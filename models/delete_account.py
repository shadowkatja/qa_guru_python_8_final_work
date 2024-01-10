from utils.helpers import send_request


def delete_account(email, password):
    endpoint = 'api/deleteAccount'
    method = 'DELETE'
    form_data = {
        'email': email,
        'password': password,
    }

    result = send_request(endpoint, method, data=form_data)
    return result
