from selenium import webdriver
from selenium.webdriver.common.by import By


from my_account_page import Constants


def test_login_user(web_driver: webdriver, login_user):
    logout_button = web_driver.find_element(*Constants.LOGOUT_BUTTON)
    assert logout_button.is_displayed()
