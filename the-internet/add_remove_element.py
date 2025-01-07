from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

def test_multiple_add_and_remove_multiple_element(browser: webdriver.Chrome):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    

    add_button =  browser.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    for _ in range(5):
        add_button.click()
    
    time.sleep(3)
    remove_buttons =  browser.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    for remove_button in remove_buttons[:4]:
        remove_button.click()
    remove_buttons =  browser.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

    assert len(remove_buttons) == 1
    # assert not browser.find_elements(By.CLASS_NAME, "added-manually")
    time.sleep(4)

def test_add_and_remove_multiple_times(browser: webdriver.Chrome):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button =  browser.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    
    for _ in range(9):
        add_button.click()
        remove_buttons =  browser.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
        remove_buttons[0].click()
    time.sleep(3)
    # remove_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    # assert len(remove_button) == 0