# Selenium autotest
Repository for stepik course about autotesting

## Credits

- Igor        (ColaChanel)      Konovalov

### FAQ:
How save requirements:
    pip freeze > requirements.txt
How install requirements:
    pip install -r requirements.txt
How to run fixtures:
    For run fixtures use command like this - 
        pytest -s environments\selenium_course\text_fixtures\test_fixture1.py
    or this test with mark - 
        pytest -s -v -m smoke  environments\selenium_course\text_fixtures\test_fixture8.py
    or thist for test without some mark -
        pytest -s -v -m "not smoke"  environments\selenium_course\text_fixtures\test_fixture8.py
    or this for tests with different marks -
        pytest -s -v -m "smoke or regression"  environments\selenium_course\text_fixtures\test_fixture8.py
For register metriks I'm using file pytest.ini
commands:
 @pytest.mark.skip - ставиться перед функцией теста и заставляет пропустить тест.
 @pytest.mark.xfail - для падающего теста.