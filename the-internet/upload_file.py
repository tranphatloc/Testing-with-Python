from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def test_upload_file(browser : webdriver.Chrome):
    driver = browser
    filename = 'test_upload.txt'
    file = os.path.join(os.getcwd(), filename) # tạo đường dẫn tuyệt đối đến file
    # print(file)
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.find_element(By.ID, 'file-upload').send_keys(file)
    driver.find_element(By.ID, 'file-submit').click()

    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, "uploaded file should be %s" %filename
    time.sleep(3)