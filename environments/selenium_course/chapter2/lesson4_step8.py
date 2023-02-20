from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import math
'''
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

'''
link = 'http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
    """
    Функция возращает результат формулы ln(abs(12*sin(x)))
    :param x:
    :return str:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
    )
    driver.find_element(By.CSS_SELECTOR, '#book').click()
    x = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(x)
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    driver.find_element(By.CSS_SELECTOR, '#solve').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()