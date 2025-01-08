from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password, expected_message",
[
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith1", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "SuperSecretPassword!1", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),

])

def test_login_page(browser : webdriver.Chrome, username, password, expected_message):
    browser.get("https://the-internet.herokuapp.com/login")

    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert expected_message in browser.page_source
    time.sleep(3)