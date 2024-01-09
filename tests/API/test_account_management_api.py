import allure
import jsonschema

from models.create_account import create_account
from models.delete_account import delete_account
from models.get_account_data_by_email import get_account_data_by_email
from models.update_account import update_account
from models.verify_login import verify_login
from test_data.test_data import auth_email, auth_password, registration_api_email, registration_api_password, COMPANY
from utils.helpers import load_schema


def test_verify_login_succesfully():
    schema = load_schema('post_verify_login.json')
    with allure.step("Send Verify user login request"):
        result = verify_login(auth_email, auth_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User exists!"
        jsonschema.validate(result.json(), schema)


def test_get_account_data_by_email_successflly():
    schema = load_schema('get_user_account_by_email.json')
    with allure.step("Send Get user account request"):
        result = get_account_data_by_email(auth_email)
    with (allure.step("Assert the result")):
        assert result.status_code == 200
        assert result.json()['user']['email'] == auth_email
        jsonschema.validate(result.json(), schema)

def test_create_account_successfully():
    schema = load_schema('post_create_user.json')
    with allure.step("Send User create request"):
        result = create_account(registration_api_email, registration_api_password)
    with allure.step("Assert the result"):
        assert result.status_code == 200
        assert result.json()["message"] == "User created!"
        jsonschema.validate(result.json(), schema)

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



