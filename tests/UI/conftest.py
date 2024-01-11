import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def set_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    adblock_path = os.path.join(root_dir, 'adblock.crx')
    options.add_extension(adblock_path)

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    site = os.getenv('SITE')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{site}",
        options=options
    )

    browser.config.driver = driver

    browser.config.base_url = 'https://automationexercise.com'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def open_browser(set_browser):
    browser.open('/')
    browser.switch_to_tab(0)
