from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

'''
1. Открыть страницу http://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное расчитанной сумме
4. Нажать кнопку "Отправить"
'''
link = 'http://suninjuly.github.io/selects1.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # Находим элемент, содержащий значение x
    num1 = driver.find_element(By.CSS_SELECTOR, '#num1').text

    # Считаем функцию со значением х
    num2 = driver.find_element(By.CSS_SELECTOR, '#num2').text

    # Передаем в поле ввода результат вычисления функции
    sum_of_nums = int(num1)+ int(num2)
    # Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    select = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown'))
    # Кликаем radio "Роботы рулят"
    select.select_by_value(str(sum_of_nums))

    # Нажимаем кнопку "Отправить"
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()