from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set up Appium Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554", 
    "appPackage": "com.facebook.katana",
    "appActivity": "com.facebook.katana.LoginActivity",
    "automationName": "UiAutomator2",
    "noReset": True 
}

# Initialize Appium Driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

time.sleep(5)  # Wait for the app to load

# Test Case 1: Login with valid credentials
def test_valid_login():
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Email address or phone number']").send_keys("your_valid_email@example.com")  # Replace with actual email
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys("your_valid_password")  # Replace with actual password
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Log In']").click()

    time.sleep(5)  # Wait for login to process
    
    # Validate successful login (Check if home feed loads)
    assert driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Home']").is_displayed()
    print("Valid Login Test Passed!")

# Test Case 2: Login with invalid credentials
def test_invalid_login():
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Email address or phone number']").send_keys("wronguser@example.com")
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys("wrongpassword")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Log In']").click()
    
    time.sleep(3)

    # Validate error message
    error_message = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'incorrect')]").text
    assert "incorrect" in error_message.lower()
    print("Invalid Login Test Passed!")

# Run tests
test_valid_login()
test_invalid_login()

# Close the App
driver.quit()
