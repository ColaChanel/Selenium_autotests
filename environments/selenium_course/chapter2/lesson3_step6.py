from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

'''
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.
Сценарий для реализации выглядит так:
1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-отве
'''
link = 'http://suninjuly.github.io/redirect_accept.html'
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
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
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