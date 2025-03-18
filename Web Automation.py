from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the login page
driver.get("https://www.saucedemo.com/")  # Replace with actual login page URL

# Maximize window
driver.maximize_window()

# Test Case 1: Login with valid credentials
def test_valid_login():
    driver.find_element(By.ID, "user-name").send_keys("problem_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)  # Wait for page load
    assert "dashboard" in driver.current_url  # Validate successful login

# Test Case 2: Login with invalid credentials
def test_invalid_login():
    driver.get("https://example.com/login")  # Reload the page
    driver.find_element(By.ID, "user-name").send_keys("wronguser")
    driver.find_element(By.ID, "passwords").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "error-message").text
    assert error_message == "Invalid credentials"  # Validate error message

# Run tests
test_valid_login()
test_invalid_login()

# Close browser
driver.quit()
