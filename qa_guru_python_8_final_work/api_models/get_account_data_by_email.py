from qa_guru_python_8_final_work.utils.helpers import send_request


def get_account_data_by_email(base_url, email):
    endpoint = "api/getUserDetailByEmail?email={}".format(email)
    method = 'GET'

    result = send_request(base_url, endpoint, method, data=None)
    return result
