import allure
from allure_commons.types import Severity

from qa_guru_python_8_final_work.pages.account_management_page import LoginPage, RegistrationPage
from qa_guru_python_8_final_work.test_data.data import user_to_registrate_ui, auth_email, auth_password

login_page = LoginPage()
registration_page = RegistrationPage()
user = user_to_registrate_ui
login = auth_email
password = auth_password


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Successful login through UI")
@allure.feature("User account")
def test_login():
    with allure.step("Open login page"):
        login_page.open_login_registration_page()
    with allure.step("Fill login form"):
        login_page.fill_login_page(login, password)
    with allure.step("Submit login"):
        login_page.submit_login()
    with allure.step("Check login"):
        login_page.check_login()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Successful logout through UI")
@allure.feature("User account")
def test_logout():
    with allure.step("Login into account"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(login, password)
        login_page.submit_login()
    with allure.step("Press logout"):
        login_page.logout()
    with allure.step("Check logout"):
        login_page.check_logout()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Successful registration of a new user through UI")
@allure.feature("User account")
def test_signup():
    with allure.step("Open registration page"):
        registration_page.open_login_registration_page()
    with allure.step("Fill short registration form"):
        registration_page.fill_first_registration_form(user)
    with allure.step("Submit short registration form"):
        registration_page.submit_first_registration_form()
    with allure.step("Fill full registration form"):
        registration_page.fill_full_registration_form(user)
    with allure.step("Submit registration"):
        registration_page.submit_registration()
    with allure.step("Check registration"):
        registration_page.check_registration()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Successful account deletion through UI")
@allure.feature("User account")
def test_delete_account():
    with allure.step("Login into account"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(user.email, user.password)
        login_page.submit_login()
    with allure.step("Press delete account"):
        registration_page.delete_account()
    with allure.step("Check deletion"):
        registration_page.check_deletion()
