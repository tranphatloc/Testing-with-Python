import pytest, time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_multiple_window(browser : webdriver.Chrome) :
    driver = browser

    driver.get("https://the-internet.herokuapp.com/windows")
    new_window = driver.find_element(By.CSS_SELECTOR, ".example a")
    new_window.click()

    driver.switch_to.window(driver.window_handles[0])
    assert driver.title == "The Internet", "title should be the Internet"
    time.sleep(3)

    WebDriverWait(driver, 2).until(lambda d: d.title != "")

    driver.switch_to.window(driver.window_handles[-1])
    assert driver.title == "New Window", "title should be the New Window"
    time.sleep(3)  