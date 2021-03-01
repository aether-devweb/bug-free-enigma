from typing import List
from error import Error
from os import system, name as distro

class Console:
    @staticmethod
    def join(inputs: List[any]):
        return ''.join(str(item) for item in list(inputs))

    @staticmethod
    def log(*inputs, end = '\n'):
        message = Console.join(inputs)
        print(f"\033[97m{message}\033[00m", end = end)
    
    @staticmethod
    def info(*inputs, end = '\n'):
        message = Console.join(inputs)
        print(f"\033[96m{message}\033[00m", end = end)

    @staticmethod
    def success(*inputs, end = '\n'):
        message = Console.join(inputs)
        print(f"\033[92m {message}\033[00m", end = end)
    
    @staticmethod
    def error(error: Error, end = '\n'):
        print(f"\033[91m{str(error)}\033[00m")

    @staticmethod
    def clear():
        system('cls' if distro == 'nt' else 'clear')

    @staticmethod
    def read_line(*prompt):
        return input(*prompt)
