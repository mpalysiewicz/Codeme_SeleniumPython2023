from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_box(web_driver: webdriver):
    item = "Black top"

    search_box = web_driver.find_element(By.ID, "search-field-top-bar")
    search_box.send_keys(item)
    search_box.submit()

    search_result = web_driver.find_element(By.XPATH, "//*[@id='main']/header/h1/span").text
    assert item.lower() == search_result.lower()


def test_check_cart(web_driver: webdriver):
    cart_button = web_driver.find_element(By.XPATH, '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    cart_button.click()
    current_url = web_driver.current_url
    expected_cart_url = "https://skleptest.pl/cart/"

    assert current_url == expected_cart_url

