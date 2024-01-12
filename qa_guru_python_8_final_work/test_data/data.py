import datetime
import os

from dotenv import load_dotenv

from qa_guru_python_8_final_work.test_data.creditcards import CreditCard
from qa_guru_python_8_final_work.test_data.users import User

COMPANY = "Red Bull"

load_dotenv()

registration_ui_email = os.getenv('REGISTRATION_UI_LOGIN')
registration_ui_password = os.getenv('REGISTRATION_UI_LOGIN')

registration_api_email: str | None = os.getenv('REGISTRATION_API_LOGIN')
registration_api_password = os.getenv('REGISTRATION_API_PASSWORD')

auth_email = os.getenv('AUTHORIZATION_LOGIN')
auth_password = os.getenv('AUTHORIZATION_PASSWORD')

card_number = os.getenv('CARD_NUMBER')
cvc = os.getenv('CVC')
expiration_month = os.getenv('EXPIRATION_MONTH')
expiration_year = os.getenv('EXPIRATION_YEAR')

incorrect_email = "brbr@test.com"
incorrect_pass = "123"

user_to_registrate_ui = User(
    name='Tifosa',
    email=registration_ui_email,
    gender='Male',
    password=registration_ui_password,
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

user_to_registrate_api = User(
    name='Max',
    email=registration_api_email,
    gender='Male',
    password=registration_api_password,
    date_of_birth=datetime.date(day=30, month=10, year=1997),
    first_name='Max',
    last_name='Verstappen',
    address='123 Avenue',
    country='United States',
    state='Texas',
    city='Austin',
    zipcode='222222',
    number='9876543210'
)

credit_card = CreditCard(
    card_holder='Charles Leclerc',
    card_number=card_number,
    cvc=cvc,
    expiration_month=expiration_month,
    expiration_year=expiration_year
)
