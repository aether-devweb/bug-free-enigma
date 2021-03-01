from error import Error, const
from console import Console
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from os import getenv
from random import randint
from dotenv import load_dotenv

load_dotenv()

account_sid = getenv('TWILIO_ACCOUNT_SID')
auth_token = getenv('TWILIO_AUTH_TOKEN')
twilio_phone = getenv('TWILIO_PHONE')
messaging_client = Client(account_sid, auth_token)

def send_otp(reciever):
    code = randint(10**5, (10**6) - 1)
    reciever = f'+91{reciever}'

    try:
        messaging_client.messages.create(
            body=f"Your authentication code is - {code}",
            from_= twilio_phone,
            to = reciever
        )

    except TwilioRestException as validationError:
        raise Error(f'Mobile Number \'{reciever}\' is not valid', const.INVALID_INPUT)

    user_input = int(input('Please enter your OTP: '))

    if not code == user_input:
        raise Error('OTP Validation Failed', const.AUTH)
    return reciever

def login_process():
    mobile = Console.read_line('Please enter your Mobile number: +91 ')
    return send_otp(mobile)
    
def login():
    while 1:
        try:
            return login_process()
        except Error as error:
            Console.error(error)
            continue