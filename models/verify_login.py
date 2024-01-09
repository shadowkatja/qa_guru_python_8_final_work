from utils.helpers import send_request

def verify_login(email, password):
    endpoint = 'api/verifyLogin'
    method = 'POST'
    form_data = {
    'email': email,
    'password': password,
}

    result = send_request(endpoint,method, data=form_data)
    return result

