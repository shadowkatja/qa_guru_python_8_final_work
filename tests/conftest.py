import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def set_browser():
    browser.config.base_url = 'https://automationexercise.com'
    browser.config.timeout = 10
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield

    browser.quit()