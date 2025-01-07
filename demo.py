from selenium import webdriver

try:
    driver = webdriver.Chrome()  # ChromeDriver sẽ tự khởi chạy nếu đã cài
    driver.get("https://www.google.com")
    print("ChromeDriver hoạt động!")
    driver.quit()
except Exception as e:
    print("Lỗi khi khởi chạy ChromeDriver:", e)