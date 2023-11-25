import json

from selenium.webdriver.common.by import By


class Constants:
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@data-product_id='17']")
    CART_BUTTON = (By.XPATH, f'//*/li[@class="top-cart"]/a')
    CART_ITEM = (By.XPATH, f'//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[@class="product-name"]/a')


def open_main_page(web_driver):
    with open('config.json') as config_file:
        data = json.load(config_file)
    web_driver.get(data['URL'])
