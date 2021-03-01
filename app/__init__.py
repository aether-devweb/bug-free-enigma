from app.database import connect_db
from auth import login
from ticket import Knox

def book_ticket(handler):
    handler.book_ticket('Coimbatore', 'Mumbai', 2300, 2400)
    pass

def retrive_ticket(handler):
    pass

def prompt():
    pass

def main():
    connection = connect_db()
    mobile = "+91 8387990021" #login()
    ticket_handler = Knox(connection, mobile)
    while 1:
        id = prompt()
        if id == 0:
            exit()
        elif id == 1:
            book_ticket(ticket_handler)
        else: retrive_ticket()
