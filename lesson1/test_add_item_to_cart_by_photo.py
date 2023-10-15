from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    by_photo_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'a[id="item_0_img_link"]')
    by_photo_add_to_cart.click()
    time.sleep(5)
    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bike-light"]')
    button_add_to_cart.click()
    time.sleep(5)

    button_cart = driver.find_element(By.CSS_SELECTOR, 'span[class="shopping_cart_badge"]')
    button_cart.click()
    time.sleep(5)