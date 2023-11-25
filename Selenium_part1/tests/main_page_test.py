from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Selenium_part1.pages.main_page_page import Constants
import Selenium_part1.pages.main_page_page as main_page
import sys


class SharedMethods:
    @staticmethod
    def clean_up_cart(web_driver: webdriver):
        item_to_remove = web_driver.find_elements(By.XPATH, f'//a[contains(@class, "remove")]')
        remove_urls = []
        for item_id in item_to_remove:
            remove_urls.append(item_id.get_attribute("href"))
        for remove_url in remove_urls:
            web_driver.get(remove_url)


def test_add_item_to_cart(web_driver: webdriver, login_user):
    main_page.open_main_page(web_driver)
    product = "Little Black Top"
    #add_to_cart_button = web_driver.find_element(By.XPATH, f"//*[normalize-space() = '{product}']//..//a") # To finish on next classes
    add_to_cart_button = web_driver.find_element(*Constants.ADD_TO_CART_BUTTON)
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constants.ADD_TO_CART_BUTTON))
    add_to_cart_button.click()
    cart_button = web_driver.find_element(*Constants.CART_BUTTON)
    cart_button.click()
    # to refactor - write better xpath and handle multiple items in the cart
    cart_item = web_driver.find_element(*Constants.CART_ITEM).text
    assert product in cart_item
    SharedMethods.clean_up_cart(web_driver)

def test_add_jeans_to_cart(web_driver: webdriver, login_user):
    product = "Asabi - Jeans"
    categories_dropdown = web_driver.find_element(By.ID, "menu-item-123")
    actions = ActionChains(web_driver)
    actions.move_to_element(categories_dropdown).perform()
    jeans_category = web_driver.find_element(By.ID, "menu-item-134")
    jeans_category.click()
    add_to_cart_button = web_driver.find_element(By.XPATH, "//a[@data-product_id='52']")
    add_to_cart_button.click()
    cart_button = web_driver.find_element(By.XPATH, f'//*/li[@class="top-cart"]/a')
    cart_button.click()
    # find all product names in cart:
    cart_items = web_driver.find_elements(By.XPATH, f'//*[@id="post-6"]/div/form/table/tbody/tr[@class="woocommerce-cart-form__cart-item cart_item"]/td[@class="product-name"]')
    # last element added to cart:
    cart_item = cart_items[0].text
    assert product in cart_item
    SharedMethods.clean_up_cart(web_driver)
