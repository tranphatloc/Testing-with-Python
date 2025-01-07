from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_gg_search():
    driver = setup()
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python")
    search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.title_contains("Python")
    )
    print(f"Current title: {driver.title}")

    assert"Python" in driver.title

    teardown(driver)



def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    return driver

def teardown(driver):
    driver.quit()