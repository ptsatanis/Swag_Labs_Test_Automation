from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_checkout():

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

    cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        )
    )
    cart.click()

    checkout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "checkout")
        )
    )

    time.sleep(2)
    checkout.click()


    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "first-name")
        )
    )

    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "last-name")
        )
    )

    postal_code = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "postal-code")
        )
    )

    first_name.send_keys("test_first_name")
    last_name.send_keys("test_last_name")
    postal_code.send_keys("test_postal_code")

    time.sleep(2)

    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "continue")
        )
    )

    continue_button.click()

    finish_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "finish")
        )
    )

    time.sleep(2)
    finish_button.click()

    back_home_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "back-to-products")
        )
    )

    time.sleep(2)
    back_home_button.click()

    driver.quit()