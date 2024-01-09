from test_data.test_data import registration_api_email, registration_api_password, user_to_registrate_api
from utils.helpers import send_request

def create_account(email, password):
    user = user_to_registrate_api
    endpoint = 'api/createAccount'
    method = 'POST'
    form_data = {
    'name': user.name,
        'email': email,
        'password': password,
        'title': "Mr" if user.gender == "Male" else "Mrs",
        'birth_date': user.date_of_birth.strftime("%d"),
        'birth_month': user.date_of_birth.strftime("%B"),
        'birth_year': str(user.date_of_birth.year),
        'firstname': user.first_name,
        'lastname': user.last_name,
        'company': "",
        'address1': user.address,
        'address2': "",
        'country': user.country,
        'zipcode': user.zipcode,
        'state': user.state,
        'city': user.city,
        'mobile_number': user.number
    }

    result = send_request(endpoint,method, data=form_data)
    return result