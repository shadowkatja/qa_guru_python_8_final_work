
from selene import have, be
from selene.support.shared import browser
class ProductManager:

    @staticmethod
    def open_product_page(self):
        browser.open('/')
        browser.element('.nav>li:nth-child(2)').click()
        return self

    def search_product(self):
        browser.element('#search_product').type('polo')
        browser.element('#submit_search').click()
        return self

    def check_search(self):
        browser.element('.productinfo text-center').should(have.text('Premium Polo T-Shirts'))
        return self


    def filter_women_dresses(self):
        browser.element('.fa').click().element('.panel-body>li:nth-child(1)').click()

    def check_filter(self):
        browser.element('.col-sm-9').should(have.text('Sleeveless Dress'))
        browser.element('.col-sm-9').should(have.text('Stylish Dress'))
        browser.element('.col-sm-9').should(have.text('Rose Pink Embroidered Maxi Dress'))

    def buy_an_item(self):
        browser.element("a[data-product-id='1']").click()
        browser.element("a[href*='/view_cart']").click()
        browser.element('.btn btn-default check_out').click()
        browser.element("a[href*='/payment']").click()
        browser.element('#submit')
        browser.element('[data-qa="name-on-card"]').send_keys('Charles Leclerc')
        browser.element('[data-qa="card-number"]').send_keys('4242424242424242')
        browser.element('[data-qa="cvc"]').send_keys('123')
        browser.element('[data-qa="expiry_month"]').send_keys('12')
        browser.element('[data-qa="expiry-year"]').send_keys('2025')

    def check_purchase(self):
        browser.element('//h2[data-qa="order-placed"]').should(have.exact_text('Order Placed!'))