from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

'''
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
'''
link = 'http://suninjuly.github.io/alert_accept.html'
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

    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    confirm = driver.switch_to.alert
    
    confirm.accept()
    # Считаем функцию со значением х
    
    x = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    calulation_result = calc(x)
    # Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(calulation_result)
    # Кликаем radio "Роботы рулят"

    # Нажимаем кнопку "Отправить"
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()