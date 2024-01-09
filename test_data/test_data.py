import datetime
import os

from dotenv import load_dotenv

from test_data.creditcards import CreditCard
from test_data.users import User

load_dotenv()

registration_email = os.getenv('REGISTRATION_LOGIN')
registration_password = os.getenv('REGISTRATION_PASSWORD')
auth_email = os.getenv('AUTHORIZATION_LOGIN')
auth_password = os.getenv('AUTHORIZATION_PASSWORD')

card_number = os.getenv('CARD_NUMBER')
cvc = os.getenv('CVC')
expiration_month = os.getenv('EXPIRATION_MONTH')
expiration_year = os.getenv('EXPIRATION_YEAR')

user_to_registrate_ui = User(
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

credit_card = CreditCard(
    card_holder='Charles Leclerc',
    card_number=card_number,
    cvc=cvc,
    expiration_month=expiration_month,
    expiration_year=expiration_year
)