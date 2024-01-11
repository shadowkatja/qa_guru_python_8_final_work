import allure
import jsonschema
import pytest
from allure_commons.types import Severity

from models.create_account import create_account
from models.delete_account import delete_account
from models.get_account_data_by_email import get_account_data_by_email
from models.update_account import update_account
from models.verify_login import verify_login
from test_data.test_data import auth_email, auth_password, registration_api_email, registration_api_password, COMPANY, \
    incorrect_email, incorrect_pass
from utils.helpers import load_schema, log_request_and_response_to_allure, log_request_and_response_to_console


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'API')
@allure.title("Login verify through API for registered and non registered user")
@allure.feature("User account")
@pytest.mark.parametrize("email,password,expected_status,response_code, expected_message", [
    (auth_email, auth_password, 200, 200, "User exists!"),
    (incorrect_email, incorrect_pass, 200, 404, "User not found!"),
])
def test_verify_login_successfully(base_url, email, password, expected_status, response_code, expected_message):
    schema = load_schema('post_verify_login.json')
    with allure.step("Send request"):
        result = verify_login(base_url, email, password)
    with allure.step("Assert the result"):
        assert result.status_code == expected_status
        assert result.json()["responseCode"] == response_code
        assert result.json()["message"] == expected_message
        jsonschema.validate(result.json(), schema)
    log_request_and_response_to_allure(result.request, result)
    log_request_and_response_to_console(result)



@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'API')
@allure.title("Get user account data by email successfully  through API")
@allure.feature("User account")
def test_get_account_data_by_email_successflly(base_url):
    schema = load_schema('get_user_account_by_email.json')
    with allure.step("Send request"):
        result = get_account_data_by_email(base_url, auth_email)
    with (allure.step("Assert the result")):
        assert result.status_code == 200
        assert result.json()['user']['email'] == auth_email
        jsonschema.validate(result.json(), schema)
    log_request_and_response_to_allure(result.request, result)
    log_request_and_response_to_console(result)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'API')
@allure.title("Create user account successfully through API")
@allure.feature("User account")
def test_create_account_successfully(base_url):
    schema = load_schema('post_create_user.json')
    with allure.step("Send request"):
        result = create_account(base_url, registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User created!"
        jsonschema.validate(result.json(), schema)
    log_request_and_response_to_allure(result.request, result)
    log_request_and_response_to_console(result)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'API')
@allure.title("Update user account data successfully through API")
@allure.feature("User account")
def test_update_account_data_successfully(base_url):
    schema = load_schema('put_update_user_account.json')
    with allure.step("Send request"):
        result = update_account(base_url, registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User updated!"
        jsonschema.validate(result.json(), schema)
    with allure.step("Check updated data"):
        result = get_account_data_by_email(base_url, registration_api_email)
        assert result.json()['user']['company'] == COMPANY
    log_request_and_response_to_allure(result.request, result)
    log_request_and_response_to_console(result)


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'API')
@allure.title("Delete user account successfully through API")
@allure.feature("User account")
def test_delete_account_successfully(base_url):
    schema = load_schema('delete_delete_account.json')
    with allure.step("Send request"):
        result = delete_account(base_url, registration_api_email, registration_api_password)
    with allure.step("Assert result"):
        assert result.status_code == 200
        assert result.json()["message"] == "Account deleted!"
        jsonschema.validate(result.json(), schema)
    with allure.step("Check deletion"):
        result = verify_login(base_url, registration_api_email, registration_api_password)
        assert result.json()["message"] == "User not found!"
    log_request_and_response_to_allure(result.request, result)
    log_request_and_response_to_console(result)
