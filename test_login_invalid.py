from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_login():

    try:
        driver = webdriver.Chrome()

        driver.get("https://www.saucedemo.com/")

        driver.implicitly_wait(10)

        username = driver.find_element(by="id", value="user-name")
        password = driver.find_element(by="id", value="password")

        username.send_keys("invalid_username")
        password.send_keys("invalid_password")

        driver.find_element(by="id", value="login-button").click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test="error"]')
            )
        )

        assert "Epic sadface: Username and password do not match any user in this service" in error.text

    finally:
        time.sleep(3)
        driver.quit()
