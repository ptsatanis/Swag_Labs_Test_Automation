from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_to_cart():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.implicitly_wait(10)

    username = driver.find_element(by="id", value="user-name")
    password = driver.find_element(by="id", value="password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    driver.find_element(by="id", value="login-button").click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        )
    )

    element.click()

    add_to_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart")
        )
    )

    add_to_cart.click()

    time.sleep(3)

    driver.quit()

