from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def test_filter():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.implicitly_wait(10)

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "user-name")
        )
    )

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "password")
        )
    )

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    driver.find_element(by="id", value="login-button").click()

    time.sleep(2)

    filter_button = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    filter_button.select_by_visible_text("Price (high to low)")

    time.sleep(2)

    driver.quit()