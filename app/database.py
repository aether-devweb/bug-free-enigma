from mysql.connector.cursor import MySQLCursor
from console import Console
from dotenv import load_dotenv
from os import getenv
from mysql.connector.connection import MySQLConnection
from mysql.connector.errors import ProgrammingError
import mysql.connector as mysql

load_dotenv()

dev = True # Change to False in Production mode

db_config = {
    'user': getenv('DB_USER'),
    'passwd': getenv('DB_PASS'),
    'host': '127.0.0.1', # ? localhost,
    'database': getenv('DB_DEV') if dev else getenv('DB_PROD')
}

def connect_db() -> MySQLConnection:
    try:
        connection = mysql.connect(**db_config)
    # This Codebase is so ugly :( but I'm not in the mood to refactor
    except ProgrammingError as error:
        if error.errno == 1045:
            Console.log('Invalid Auth Credentials')

        elif error.errno == 1049:
            Console.log('Database Does not exist. Migration required')

        else:
            Console.log('Something went wrong :(')

        exit()

    Console.log('DB Connection Sucessfull')
    return connection
