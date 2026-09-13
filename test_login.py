from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.implicitly_wait(10)

    username = driver.find_element(by="id", value="user-name")
    password = driver.find_element(by="id", value="password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    driver.find_element(by="id", value="login-button").click()

    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()