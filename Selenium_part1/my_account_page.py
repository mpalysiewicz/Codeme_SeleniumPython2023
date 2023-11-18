from selenium import webdriver
from selenium.webdriver.common.by import By


class Constants:
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='top-account']")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div/main/article/div[2]/nav/ul/li[6]/a")
