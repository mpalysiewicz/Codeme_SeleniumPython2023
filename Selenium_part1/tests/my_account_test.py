from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Selenium_part1.pages.my_account_page import Constants
import sys


def test_login_user(web_driver: webdriver, login_user):
    logout_button = web_driver.find_element(*Constants.LOGOUT_BUTTON)
    assert logout_button.is_displayed()
    print(sys.path)


def test_user_registration(web_driver: webdriver, create_user_with_credentials):
    user = create_user_with_credentials
    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constants.EMAIL_INPUT_REG).send_keys(user.email)
    web_driver.find_element(*Constants.PASSWORD_INPUT_REG).send_keys(user.password)
    web_driver.find_element(*Constants.REG_LABEL).click()
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constants.REG_BUTTON))
    web_driver.find_element(*Constants.REG_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constants.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constants.HELLO_MESSAGE).text
    assert user.first_name and user.last_name in hello_message, \
        f"{user.first_name} and {user.last_name} does not present in {hello_message}"
