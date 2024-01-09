
from selene import have, be, command
from selene.support.shared import browser

from test_data.creditcards import CreditCard


class ProductManager:

    @staticmethod
    def open_product_page():
        browser.open('/')
        browser.element('.nav>li:nth-child(2)').click()

    def search_product(self):
        browser.element('#search_product').type('polo')
        browser.element('#submit_search').click()
        return self

    def check_search(self):
        browser.element('.product-image-wrapper').perform(command.js.scroll_into_view)
        browser.element('.product-image-wrapper').should(have.text('Premium Polo T-Shirts'))
        return self


    def filter_women_dresses(self):
        browser.element('[data-toggle="collapse"]').click()
        browser.element('a[href="/category_products/1"]').click()

    def check_filter(self):
        browser.element('.features_items').perform(command.js.scroll_into_view)
        browser.element('.features_items').should(have.text('Sleeveless Dress'))
        browser.element('.features_items').should(have.text('Stylish Dress'))
        browser.element('.features_items').should(have.text('Rose Pink Embroidered Maxi Dress'))

    def purchase_an_item(self, creditcard: CreditCard):
        browser.element("a[data-product-id='1']").click()
        browser.element("a[href='/view_cart']").click()
        browser.element('.btn btn-default check_out').click()
        browser.element('a[href="/payment"]').perform(command.js.scroll_into_view)
        browser.element('a[href="/payment"]').click()
        browser.element('[data-qa="name-on-card"]').send_keys('Charles Leclerc')
        browser.element('[data-qa="card-number"]').send_keys('4242424242424242')
        browser.element('[data-qa="cvc"]').send_keys('123')
        browser.element('[data-qa="expiry_month"]').send_keys('12')
        browser.element('[data-qa="expiry-year"]').send_keys('2025')
        browser.element('#submit')

    def check_purchase(self):
        browser.element('[data-qa="order-placed"]').should(have.text('ORDER PLACED!'))