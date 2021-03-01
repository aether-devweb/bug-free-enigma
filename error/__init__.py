from datetime import datetime

def get_curtime():
    return datetime.now().strftime('%H:%M')

class Error(Exception):
    def __init__(self, message, status = 0, severity = 'Extreame'):
        self.message = message
        self.status = status

    def __str__(self) -> str:
        return f'[EXCEPTION {self.status} on {get_curtime()}] {self.message}'
    
    def __repr__(self) -> str:
        return super().__repr__()
