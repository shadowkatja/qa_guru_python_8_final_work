from utils.helpers import send_request

def get_account_data_by_email(email):
    endpoint = "api/getUserDetailByEmail?email={}".format(email)
    method = 'GET'


    result = send_request(endpoint,method, data=None)
    return result