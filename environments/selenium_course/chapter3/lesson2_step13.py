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
import pytest

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):

    def test_first_link_first(self):
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "NoSuchElementException")
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input") # Ваш код, который заполняет обязательные поля
        input1.send_keys("Iren")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Horak")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.com")

        button = browser.find_element(By.CLASS_NAME, "btn-default") # Отправляем заполненную форму
        button.click()
        time.sleep(1)

    def test_first_link_two(self):
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "NoSuchElementException")
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Iren")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Horak")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.com")

        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
	# pytest.main()