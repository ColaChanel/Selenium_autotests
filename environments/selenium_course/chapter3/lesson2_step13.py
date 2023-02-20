"""
https://stepik.org/lesson/36285/step/13?unit=162401
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.
Возьмите тесты из шага 10 - https://stepik.org/lesson/138920/step/10?unit=196194
Создайте новый файл
Создайте в нем класс тестов unittest
Добавьте тест для страницы http://suninjuly.github.io/registration1.html﻿
Добавьте второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest


class test_reg_page(unittest.TestCase):
	def test_registration_page_1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
		input1.send_keys("Ivan")

		input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
		input2.send_keys("Petrov")

		input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
		input3.send_keys("Smolensk")


		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		time.sleep(1)


		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration page #1 — not passed")

        
	def test_registration_page_2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
		input1.send_keys("Ivan")

		input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
		input2.send_keys("Petrov")

		input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
		input3.send_keys("Smolensk")


		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		time.sleep(1)


		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Registration page #2 — not passed")


if __name__ == '__main__':
	unittest.main()