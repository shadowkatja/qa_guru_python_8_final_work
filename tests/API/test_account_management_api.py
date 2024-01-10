import allure
import jsonschema
from allure_commons.types import Severity

from models.create_account import create_account
from models.delete_account import delete_account
from models.get_account_data_by_email import get_account_data_by_email
from models.update_account import update_account
from models.verify_login import verify_login
from test_data.test_data import auth_email, auth_password, registration_api_email, registration_api_password, COMPANY
from utils.helpers import load_schema, log_request_and_response_to_allure


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.title("Successful login verify")
@allure.feature("Accounts")
def test_verify_login_succesfully():
    schema = load_schema('post_verify_login.json')
    with allure.step("Send Verify user login request"):
        result = verify_login(auth_email, auth_password)
        log_request_and_response_to_allure(result.request, result)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User exists!"
        jsonschema.validate(result.json(), schema)

@allure.tag("api")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Get account data by email")
@allure.feature("Accounts")
def test_get_account_data_by_email_successflly():
    schema = load_schema('get_user_account_by_email.json')
    with allure.step("Send Get user account request"):
        result = get_account_data_by_email(auth_email)
    with (allure.step("Assert the result")):
        assert result.status_code == 200
        assert result.json()['user']['email'] == auth_email
        jsonschema.validate(result.json(), schema)

@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.title("Create an account")
@allure.feature("Accounts")
def test_create_account_successfully():
    schema = load_schema('post_create_user.json')
    with allure.step("Send User create request"):
        result = create_account(registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User created!"
        jsonschema.validate(result.json(), schema)

@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.title("Update account data")
@allure.feature("Accounts")
def test_update_account_data_successfully():
    schema = load_schema('put_update_user_account.json')
    with allure.step("Send Account update request"):
        result = update_account(registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User updated!"
        jsonschema.validate(result.json(), schema)
    with allure.step("Check updated data"):
        result = get_account_data_by_email(registration_api_email)
        assert result.json()['user']['company'] == COMPANY


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.title("Delete account")
@allure.feature("Accounts")
def test_delete_account_succesfully():
    schema = load_schema('delete_delete_account.json')
    with allure.step("Send Account delete request"):
        result = delete_account(registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "Account deleted!"
        jsonschema.validate(result.json(), schema)
    with allure.step("Check deletion"):
        result = verify_login(registration_api_email, registration_api_password)
        assert result.json()["message"] == "User not found!"



