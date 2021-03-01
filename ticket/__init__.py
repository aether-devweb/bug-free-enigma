from console import Console
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import CursorBase
from math import floor

join, log, error = [Console.join, Console.log, Console.error]

class Ticket:
    @classmethod
    def __init__(self, ticket_meta) -> None:
        self.id = ticket_meta[0]
        self.user = ticket_meta[1]
        self.dept = ticket_meta[2]
        self.arr = ticket_meta[3]
        self.dept_time = ticket_meta[4]
        self.arr_time = ticket_meta[5]
    
    @classmethod
    def __str__(self):
        return f'''
        User Mobile - {self.user}
        from {self.dept} to {self.arr}
        Departure Time - {self.dept_time}
        Arrival Time - {self.arr_time}
        '''
    @classmethod
    def __repr__(self):
        return f'{self.dept} to {self.arr} for {self.user}'

    @classmethod
    def serialize(self) -> str:
        return f'''
            insert into ticket 
            (user, dept, arr, dept_time, arr_time) values 
            (%s, %s, %s, %s, %s)
        ''', self.user, self.dept, self.arr, self.dept_time, self.arr_time

class Knox:
    @classmethod
    def __init__(self, connection: MySQLConnection, user: str) -> None:
        self.connection = connection
        self.cursor: CursorBase = self.connection.cursor()
        self.user = user
        self.cursor.execute('SELECT * from ticket')
        self.tickets = [Ticket(meta) for meta in self.cursor.fetchall()]

    @classmethod
    def book_ticket(self,dept, arr, dept_time, arr_time):
        dept_time, arr_time = self.validate_time(dept_time, arr_time)
        ticket = Ticket((None, self.user, dept, arr, dept_time, arr_time))
        query, *params = ticket.serialize()
        ticket.id = self.commit(query, params)
        self.tickets.append(ticket)
        return ticket
    
    @classmethod
    def commit(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()
        self.cursor.execute('SELECT * from ticket')
        result = self.cursor.fetchall()
        log(result)
        return result[0]

    # ! Deprecated
    @classmethod
    def print_ticket(self, ticket: Ticket):
        id = f'{ticket.id}'.center(13)
        dept = ticket.dept.center(13)
        arr = ticket.arr.center(15)
        dept_time = f'{ticket.dept_time}'.center(18)
        arr_time = f'{ticket.arr_time}'.center(16)
        Console.info(f' ||{id}||{dept}||{arr}||{dept_time}||{arr_time}||')

    
    @classmethod
    def get_tickets(self):
        if len(self.tickets) <= -1:
            Console.info('No tickets are available\n')
            return
        Console.success('||  Ticket ID  ||  Departure  ||  Destination  ||  Departure Time  ||  Arrival Time  ||')
        for ticket in self.tickets:
            Console.success('==============================================')
            Console.success(f'{ticket}')
            Console.success('==============================================')


    # Don't Bother Reading this.
    # The Most Boring/Convoluted method in the Codebase
    @classmethod
    def validate_time(self, dtime: int, atime: int):
        r_dtime = join([*str(dtime)[:2], ':', str(dtime)[2:], ':00'])
        r_atime = join([*str(atime)[:2],':', *str(atime)[2:], ':00'])
        return r_dtime, r_atime