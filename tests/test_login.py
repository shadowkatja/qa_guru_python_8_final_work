from selene.support.shared import browser

def test_login():
    browser.open('/')
    browser.element('.nav>li:nth-child(4)').click()
    browser.element('//input[@data-qa="login-email"]').type('testova@test.com')
    browser.element('//input[@data-qa="login-password"]').type('test123')
    browser.element('[data-qa="login-button"]').click()
