# Automated Login Test using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver Chrome in this example
driver = webdriver.Chrome()

try:
    # Open the login page 
    driver.get("https://example.com/login")

    time.sleep(2)  # Let the page load

    # Locate username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Valid Credentials Test
    username_field.send_keys("valid_user")
    password_field.send_keys("valid_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    print(" Valid login test completed")

    # Log out if necessary (replace selector)
    # driver.find_element(By.ID, "logout-button").click()

    driver.get("https://example.com/login")
    time.sleep(2)

    # Invalid Credentials Test
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("invalid_user")
    password_field.send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    print(" Invalid login test completed")

finally:
    driver.quit()
