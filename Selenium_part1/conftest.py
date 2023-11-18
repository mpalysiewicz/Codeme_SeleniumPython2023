import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from my_account_page import Constants


@pytest.fixture
def web_driver() -> webdriver:
    driver = webdriver.Chrome()
    driver.get("https://skleptest.pl")
    driver.maximize_window()
    driver.implicitly_wait(10)


    yield driver
    driver.quit()

    ## driver.close()

@pytest.fixture(autouse=False)
def login_user(web_driver):
    user_name = 'test_selenium@wp.pl'
    password_name = 'Test1234567#$%@'

    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()

    username_input = web_driver.find_element(*Constants.USERNAME_INPUT)
    passwordname_input = web_driver.find_element(*Constants.PASSWORD_INPUT)

    username_input.clear()
    username_input.send_keys(user_name)
    passwordname_input.clear()
    passwordname_input.send_keys(password_name)

    web_driver.find_element(*Constants.LOGIN_BUTTON).click()
