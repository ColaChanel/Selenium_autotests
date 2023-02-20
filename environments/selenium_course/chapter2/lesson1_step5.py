from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/math.html'


def calc(x):
    '''
    Функция возращает результат формулы
    :param x:
    :return:
    '''
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get(link)

    # Находим элемент, содержащий значение x
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')

    # Получаем текст внутри этого элемента
    x = x_element.text

    # Считаем функцию со значением х
    y = calc(x)

    # Передаем в поле ввода результат вычисления функции
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    # Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    driver.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    # Кликаем radio "Роботы рулят"
    driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    # Нажимаем кнопку "Отправить"
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()