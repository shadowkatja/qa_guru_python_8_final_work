import datetime
import os

from dotenv import load_dotenv

from users.users import User

load_dotenv()

registration_email = os.getenv('REGISTRATION_LOGIN')
registration_password = os.getenv('REGISTRATION_PASSWORD')
auth_email = os.getenv('AUTHORIZATION_LOGIN')
auth_password = os.getenv('AUTHORIZATION_PASSWORD')

user_to_registrate = User(
    name='Tifosa',
    email=registration_email,
    gender='Male',
    password=registration_password,
    date_of_birth=datetime.date(day=16, month=10, year=1997),
    first_name='Charles',
    last_name='Leclerc',
    address='123 Avenue',
    country='United States',
    state='Texas',
    city='Austin',
    zipcode='11111',
    number='1234567890'
)
