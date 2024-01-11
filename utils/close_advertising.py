from selene import be, command
from selene.support.shared import browser

def close_advertising():
    if browser.with_(timeout=10).element('#aswift_5_host').matching(be.visible):
        browser.with_(timeout=10).element('#aswift_5_host').should(be.visible).perform(command.js.remove)
    if browser.with_(timeout=10).element('.adsbygoogle adsbygoogle-noablate').matching(be.visible):
        browser.with_(timeout=10).element('.adsbygoogle adsbygoogle-noablate').should(be.visible).perform(command.js.remove)
    if browser.with_(timeout=10).element('#google_esf').matching(be.visible):
        browser.with_(timeout=10).element('#google_esf').should(be.visible).perform(command.js.remove)
    recaptcha_iframe = browser.with_(timeout=10).element('iframe[src="https://www.google.com/recaptcha/api2/aframe"]')
    if recaptcha_iframe.matching(be.in_dom):  # Check if the iframe is present in the DOM
        recaptcha_iframe.perform(command.js.remove)
