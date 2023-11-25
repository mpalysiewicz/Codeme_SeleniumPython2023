from selenium.webdriver.common.by import By


class Constants:
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='top-account']")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div/main/article/div[2]/nav/ul/li[6]/a")

    REG_BUTTON = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    HELLO_MESSAGE = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")

    EMAIL_INPUT_REG = (By.XPATH, "//input[@id='reg_email']")
    PASSWORD_INPUT_REG = (By.XPATH, "//input[@id='reg_password']")
    REG_LABEL = (By.XPATH, "//h2[contains(text(),'Register')]")
