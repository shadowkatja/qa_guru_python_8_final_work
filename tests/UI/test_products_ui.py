import allure
from allure_commons.types import Severity

from pages.account_management_page import LoginPage
from pages.product_page import ProductManager
from test_data import test_data

product_page = ProductManager()
login_page = LoginPage()
login = test_data.auth_email
password = test_data.auth_password
credit_card = test_data.credit_card


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Check search")
@allure.feature("Search")
def test_search():
    with allure.step("Open products page"):
        product_page.open_product_page()
    with allure.step("Search 'Polo' item"):
        product_page.search_product()
    with allure.step("Check search result"):
        product_page.check_search()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Filter women dresses items")
@allure.feature("Filters")
def test_filters():
    with allure.step("Open products page"):
        product_page.open_product_page()
    with allure.step("Filter women dresses"):
        product_page.filter_women_dresses()
    with allure.step("Check filter"):
        product_page.check_filter()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "e.goldinova")
@allure.label('layer', 'WEB')
@allure.title("Purchase")
@allure.feature("Purchasing")
def test_purchase():
    with allure.step("Login into account"):
        login_page.open_login_registration_page()
        login_page.fill_login_page(login, password)
        login_page.submit_login()
    with allure.step("Open products page"):
        product_page.open_product_page()
    with allure.step("Add item 'Blue top' to cart"):
        product_page.add_item_to_cart()
    with allure.step("Confirm purchase"):
        product_page.confirm_purchase()
    with allure.step("Fill payment data"):
        product_page.fill_card_data(credit_card)
    with allure.step("Pay for the chosen item"):
        product_page.pay_for_chosen_item()
    with allure.step("Check purchase"):
        product_page.check_purchase()
