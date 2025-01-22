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


def test_multiple_window_dienmayxanh(browser : webdriver.Chrome):
    driver = browser
    driver.get("https://www.dienmayxanh.com/")
    bachhoaxanh =  driver.find_element(By.XPATH, '/html/body/footer/section/div[4]/div[1]/div/ul/li[3]/a').click()
    driver.switch_to.window(driver.window_handles[0])
    assert driver.title == 'Siêu thị Điện máy XANH - Mua bán điện tử, điện lạnh, gia dụng', 'Khong dung cua so'
    time.sleep(3)
    nhathuocankhang = driver.find_element(By.XPATH, '/html/body/footer/section/div[4]/div[1]/div/ul/li[4]/a').click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 2).until(lambda d: d.title != "")

    assert driver.title =='Siêu thị Bách hoá XANH - Mua bán thực phẩm, sản phẩm gia đình', 'Khong dung cua so'
    time.sleep(2)
    WebDriverWait(driver, 2).until(lambda d: d.title != "")

    driver.switch_to.window( )
    assert driver.title == 'Nhà thuốc An Khang - thành viên tập đoàn Thế Giới Di Động - Nhathuocankhang.com', 'Khong dung cua so'
    windows_id = driver.window_handles

    for  window_id in  windows_id:
        driver.switch_to.window(window_id)
        print(f"cửa sổ {window_id}, có title: {driver.title}, có URL: {driver.current_url}")

    time.sleep(2)
    