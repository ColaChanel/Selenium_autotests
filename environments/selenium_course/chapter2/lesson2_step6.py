from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

'''
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "Подтверждаю, что являюсь роботом".
7. Переключить radiobutton "Роботы рулят!".
8. Нажать на кнопку "Отправить".
'''
link = 'https://suninjuly.github.io/execute_script.html'

def calc(x):
    """
    Функция возращает результат формулы
    :param x:
    :return:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    # Считаем функцию со значением х
    y = calc(x)

    # Передаем в поле ввода результат вычисления функции
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    # Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    # Кликаем radio "Роботы рулят"
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    # Нажимаем кнопку "Отправить"
    driver.execute_script('return arguments[0].scrollIntoView(true);', button)

    # Кликаем radio "Роботы рулят"
    driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    # Нажимаем кнопку "Отправить"
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()