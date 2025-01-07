from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_remove_element(browser :  webdriver.Chrome):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    

    add_button =  browser.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_button.click()
    
    time.sleep(3)
    remove_button =  browser.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert remove_button.is_displayed
    remove_button.click()
    assert not browser.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

    # assert not browser.find_elements(By.CLASS_NAME, "added-manually")
    time.sleep(4)

