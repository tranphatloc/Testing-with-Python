from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import pytest,time ,os, tempfile, shutil

@pytest.fixture
def setup_teardown():
    download_dir = tempfile.mkdtemp() # tạo thư mục tạm, thư mục này sẽ chứa các file tải về và thư mục này sẽ được xóa bởi 1 thư viện khác sao khi chạy xong test.
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,  # thư mục tải file về
        "download.prompt_for_download": False,       # tắt hộp thoại xác nhận tải xuống
        "download.directory_upgrade": True,         # tự động nâng cấp đường dẫn
        "plugins.always_open_pdf_externally": True  # tải PDF thay vì mở trực tiếp
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    yield driver, download_dir

    driver.quit()
    shutil.rmtree(download_dir) #xóa thư mục tạm

def test_file_download(setup_teardown: tuple[webdriver.Chrome, str]):
    driver , download_dir = setup_teardown
    driver.get("https://the-internet.herokuapp.com/download")
    download_link = driver.find_element(By.CSS_SELECTOR, "div.example a")
    download_link.click()
    time.sleep(2)
    try:
        WebDriverWait(driver, 5).until(lambda d: os.listdir(download_dir))
    except TimeoutException:
        assert False, "No files were download within 5 seconds."
    files = os.listdir(download_dir)
    #print("f: ", files) #f:  ['20MB.bin.crdownload']
    files = [os.path.join(download_dir, f) for f in files]
    # print("fs: ", files) #fs:  ['C:\\Users\\tranp\\AppData\\Local\\Temp\\tmph6ytdks1\\20MB.bin.crdownload']

    assert len(files) > 0, "No files were download"
    assert os.path.getsize(files[0]) > 0, "Download files was emty" 
    time.sleep(3)

