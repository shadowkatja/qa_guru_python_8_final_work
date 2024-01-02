from selene.support.shared import browser
from selene import have, be


class AccountManager:
    @staticmethod
    def open_login_page(self):
        browser.open('/')
        browser.element('.nav>li:nth-child(4)').click()
        return self

    @staticmethod
    def logout(self):
        browser.element('.nav>li:nth-child(4)').click()

    def check_logout(self):
        browser.element('.login-form').should(have.text('Login to your account'))
    @staticmethod
    def delete_account(self):
        browser.element('.nav>li:nth-child(5)').click()

    def check_account_delete
        browser.element('//h2[data-qa="account-deleted"]').should(have.exact_text('Account Deleted!'))





class LoginPage(AccountManager):

    def fill_login_form(self, login, password):
        browser.element('//input[@data-qa="login-email"]').type(login)
        browser.element('//input[@data-qa="login-password"]').type(password)
        return self

    @staticmethod
    def submit_login(self):
        browser.element('[data-qa="login-button"]').click()

    def check_login(self):
        browser.element('.nav>li:nth-child(4)').should(be.visible)
        browser.element('.nav>li:nth-child(10)').should(have.text('Logged in as'))


class RegistrationPage(AccountManager):

    def fill_simple_main_registration_form(self, name, email):
        browser.element('//input[@data-qa="signup-name"]').type(name)
        browser.element('//input[@data-qa="signup-email"]').type(email)
        return self

    @staticmethod
    def submit_simple_registration_form(self):
        browser.element('[data-qa="signup-button"]').click()

    def fill_full_registration_form(self):
        browser.element('#id_gender2').click()
        browser.element('#password').type('123')
        browser.element('#days').send_keys('12')
        browser.element('#months').send_keys('February')
        browser.element('#years').send_keys('1994')

        browser.element('#first_name').type('User')
        browser.element('#last_name').type('Test')
        browser.element('#address1').type('123 Test Address')
        browser.element('#country').send_keys('United States')
        browser.element('#state').type('Texas')
        browser.element('#city').type('Austin')
        browser.element('#zipcode').type("11111")
        browser.element('#mobile_number').type("1234567890")

        return self

    def submit_registration(self):
        browser.element('[data-qa="create-account"]').click()

    def check_registration(self):
        browser.element('//h2[data-qa="account-created"]').should(have.exact_text('Account Created!'))
