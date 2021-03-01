from app.database import connect_db
from auth import login
from ticket import Knox
from console import Console
from error import Error
from time import sleep

def normalize_time(time_param: int):
    return time_param if time_param < 2400 else time_param - 2400

def book_ticket(handler):
    arr = Console.read_line('Where would you like to go?')
    dept = Console.read_line('Where does your Voyage start?')
    dept_time = int(Console.read_line('When would you like to start your journey? Please enter your choice in HHMM format.'))
    arr_time = dept_time + 400
    arr_time = normalize_time(arr_time)
    Console.success(f'Booking Sucessfull\n{handler.book_ticket(dept, arr, dept_time, arr_time)}')
    Console.read_line('Press enter key to continue')
    sleep(.5)

def retrive_ticket(handler):
    Console.clear()
    handler.get_tickets()
    Console.read_line('Press enter key to continue')
    sleep(.5)

def prompt():
    retries = 2
    while 1:
        prompts = ['Buy Tickets (b)', 'Retrive Ticket (r)', 'Quit (q)']
        options = [
            ['b', 'B','1', prompts[0]], 
            ['r', 'R', '2', prompts[1]],
            ['q', 'Q', '3', prompts[2]]
        ]
        for item in prompts:
            Console.success(prompts.index(item) + 1, '. ', item)
        choice = Console.read_line('Choice')
        if choice not in 'bBrRqQ123':

            Console.clear()
            if retries >= 0:
                Console.error(Error(f'I couldn\'t understand \'{choice}\'. Choose Again', 0))
            else:
                Console.error(Error(f'Dude?? Seriously? It\'s so simple, where do you see \'{choice}\' in those options.'))
            retries -= 1
            continue

        for option in options:
            if choice in option:
                return prompts.index(option[3])

def shutdown():
    Console.clear()
    Console.success('\nGracefully Shutting Down :)\n')
    sleep(.5)
    Console.clear()
    exit()


def main():
    connection = connect_db()
    mobile = login()
    ticket_handler = Knox(connection, mobile)
    while 1:
        Console.clear()
        id = prompt()
        Console.clear()

        if id == 0:
            book_ticket(ticket_handler)

        elif id == 1:
            retrive_ticket(ticket_handler)

        elif id == 2: 
            shutdown()
        continue
