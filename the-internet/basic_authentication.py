from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_basic_auth(browser : webdriver.Chrome):
    username = "admin"
    password = "admin"
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    browser.get(url)
    success_message = browser.find_element(By.CSS_SELECTOR, "div.example p").text
    assert success_message == "Congratulations! You must have the proper credentials." , \
        f"Expected success message not found. Found: {success_message}"
    time.sleep(4)