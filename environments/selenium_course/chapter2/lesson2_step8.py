from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

'''
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Отправить"
'''
link = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Ivan')
    driver.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Petrov')
    driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email@email.com')
    # Считаем функцию со значением х
    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, 'file.txt')
    # Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    upload_element = driver.find_element(By.CSS_SELECTOR, '#file')
    # Кликаем radio "Роботы рулят"
    upload_element.send_keys(file_path)

    # Нажимаем кнопку "Отправить"
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()