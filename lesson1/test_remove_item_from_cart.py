from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_remove_item_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()
    time.sleep(5)

    button_cart = driver.find_element(By.CSS_SELECTOR, 'span[class="shopping_cart_badge"]')
    button_cart.click()
    time.sleep(5)

    item = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"]>div[class="inventory_item_name"]').text
    print(item)

    button_remove_item = driver.find_element(By.CSS_SELECTOR, 'button[id="remove-sauce-labs-backpack"]')
    button_remove_item.click()
    time.sleep(5)

    item_after = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"]>div[class="inventory_item_name"]').text
    print(item_after)
    assert item != item_after
