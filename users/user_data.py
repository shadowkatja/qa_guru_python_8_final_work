import datetime
import os

from dotenv import load_dotenv

from users.users import User

load_dotenv()

email = os.getenv('REGISTRATION_LOGIN')
password = os.getenv('REGISTRATION_PASSWORD')

user_to_registrate = User(
    name='Tifosa',
    email=email,
    gender='Male',
    password=password,
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
