import json
import string
from dataclasses import dataclass
from random import choice

import names
import pytest
from selenium import webdriver


from Selenium_part1.pages.my_account_page import Constants

@dataclass
class User:
    """The simple data class for User."""
    first_name: str
    last_name: str
    email: str
    password: str

@pytest.fixture
def web_driver(config) -> webdriver:
    if config["BROWSER"] == 'Chrome':
        driver = webdriver.Chrome()
    elif config["BROWSER"] == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f'"{config["Browser"]} is not a supported browser')
    driver.get(config["URL"])
    driver.maximize_window()
    driver.implicitly_wait(10)


    yield driver
    driver.quit()

    ## driver.close()

@pytest.fixture(autouse=False)
def login_user(web_driver: web_driver) -> webdriver:
    user_name = 'test_selenium@wp.pl'
    password_name = 'Test1234567#$%@'

    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    username_input = web_driver.find_element(*Constants.USERNAME_INPUT)
    username_input.clear()
    username_input.send_keys(user_name)
    passwordname_input = web_driver.find_element(*Constants.PASSWORD_INPUT)
    passwordname_input.clear()
    passwordname_input.send_keys(password_name)

    web_driver.find_element(*Constants.LOGIN_BUTTON).click()

@pytest.fixture
def create_user_with_credentials(generate_password: str):

    first_name = names.get_first_name()
    last_name = names.get_last_name()
    email = f"{first_name}.{last_name}@gmail.com"
    return User(first_name, last_name, email, generate_password)

@pytest.fixture
def generate_password() -> str:
    """Generate password with ten letters, ten digits and ten punctuation e.g. KkQkIGmsVx1530668957(|+$,_('~{"""
    return "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10)) + \
           "".join(choice(string.punctuation) for i in range(10))

@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data
