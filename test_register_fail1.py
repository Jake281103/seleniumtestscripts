import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="function")
def setup_browser():  
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver
    # Remove the driver.quit() to keep browser open

def test_register_fail(setup_browser):  
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/")
    driver.set_window_size(1200,1000)

    # Wait for Register As Mentor link to appear
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register As Mentor")))

    driver.find_element(By.LINK_TEXT, "Register As Mentor").click()

    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("thawmaungoogmail.com")
    driver.find_element(By.NAME, "first_name").click()
    driver.find_element(By.NAME, "first_name").send_keys("1213")
    driver.find_element(By.NAME, "last_name").click()
    driver.find_element(By.NAME, "last_name").send_keys("1212")
    driver.find_element(By.ID, "company").click()
    driver.find_element(By.ID, "company").send_keys("ABC")
    driver.find_element(By.ID, "expertise").click()
    driver.find_element(By.ID, "expertise").send_keys("DEFG")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.NAME, "password_confirmation").click()
    driver.find_element(By.NAME, "password_confirmation").send_keys("123456")

    # Wait for the register button to be clickable
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-btn")))

    # Scroll the button into view to avoid interception
    driver.execute_script("arguments[0].scrollIntoView(true);", register_button)

    # Wait for a moment to ensure the page finishes rendering
    time.sleep(3)  # Adjust this if necessary

    # Click the register button
    register_button.click()

    # Assert the default browser validation message
    email_field = driver.find_element(By.ID, "email")
    validation_message = driver.execute_script("return arguments[0].validationMessage;", email_field)

    # Debugging output: Print the validation message in the console
    # print(f"Validation message: {validation_message}")

    # Expected default message for invalid email
    expected_message = "Please include an '@' in the email address. 'thawmaungoogmail.com' is missing an '@'."
    
    # Add an infinite loop to keep the browser open
    while True:
        time.sleep(1)
        if validation_message == expected_message:
            print("✅ Test Success: Email validation is working correctly!")
            print(f"✅ Received expected error message: {validation_message}")
            break
        else:
            print(f"❌ Test Failed: Expected '{expected_message}', but got '{validation_message}'")
            break
