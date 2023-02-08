from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\igorv\OneDrive\Documents\GitHub\Selenium_autotests\environments\yandex_driver\yandexdriver.exe")
driver = webdriver.Chrome(service=s)
options = webdriver.ChromeOptions()
# binary_yandex_driver_file = r"C:\Users\igorv\OneDrive\Documents\GitHub\Selenium_autotests\environments\yandex_driver\yandexdriver.exe"
# driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")
time.sleep(5)
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
time.sleep(5)
driver.quit()