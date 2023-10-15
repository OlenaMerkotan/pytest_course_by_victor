

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_successfull_transition_to_link_of_item():
    driver.get("https://www.saucedemo.com/inventory.html")

    # username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    # username_field.send_keys("standard_user")
    #
    # password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    # password_field.send_keys("secret_sauce")
    #
    # login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    # login_button.click()

    sause_lab_backpag_button = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    sause_lab_backpag_button.click()
    time.sleep(5)
    # assert sause_lab_backpag_button.current_url = "https://www.saucedemo.com/inventory-item.html?id=4"