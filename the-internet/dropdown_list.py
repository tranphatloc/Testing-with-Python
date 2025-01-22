import pytest, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_dropdown(browser: webdriver.Chrome): #tìm phần tử trong danh sách bằng cách lập qua các phần tử
    driver = browser
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_list = driver.find_element(By.ID, 'dropdown')
    options_list = dropdown_list.find_elements(By.TAG_NAME,'option')

    for opt in options_list:
        if opt.text == 'Option 2':
            opt.click()
            break
    for opt in options_list:
        if opt.is_selected():
            select_option = opt.text
            break
    assert select_option == 'Option 2','Selected option should be Option 2'
    time.sleep(3)
def test_dropdown2(browser: webdriver.Chrome): #Tìm phần tử trong danh sách sử dụng tiện ích selenium.webdriver.support.select
    driver = browser
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_list = driver.find_element(By.ID, 'dropdown')
    select_list = Select(dropdown_list)
    select_list.select_by_visible_text('Option 1')
    select_option = select_list.first_selected_option.text
    assert select_option == 'Option 1', 'Selected option should be Option 1'
    time.sleep(3)
