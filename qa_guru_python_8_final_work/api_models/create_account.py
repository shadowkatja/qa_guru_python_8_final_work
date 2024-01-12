from qa_guru_python_8_final_work.test_data.data import user_to_registrate_api
from qa_guru_python_8_final_work.utils.helpers import send_request


def create_account(base_url, email, password):
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

    result = send_request(base_url, endpoint, method, data=form_data)
    return result
