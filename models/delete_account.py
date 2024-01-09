from test_data.test_data import registration_api_email, registration_api_password
from utils.helpers import send_request

def delete_account(email, password):
    endpoint = 'api/deleteAccount'
    method = 'DELETE'
    form_data = {
    'email': email,
    'password': password,
}

    result = send_request(endpoint,method, data=form_data)
    return result