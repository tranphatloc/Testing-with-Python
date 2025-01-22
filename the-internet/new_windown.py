import pytest, time

from selenium import webdriver
from selenium.webdriver.common.by import By



def test_new_window(browser: webdriver.Chrome):
    driver = browser
    driver.get('https://the-internet.herokuapp.com/windows')
    time.sleep(2)
    driver.switch_to.new_window('window')
    time.sleep(4)
    driver.get('https://the-internet.herokuapp.com/typos')
    assert len(driver.window_handles) == 2
    time.sleep(4)