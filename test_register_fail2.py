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
    driver.quit()

def test_register_fail(setup_browser):  
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/")
    driver.set_window_size(1200, 1000)

    # Wait for Register As Mentor link to appear and click it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register As Mentor"))).click()

    # Fill in the form with test data
    driver.find_element(By.ID, "email").send_keys("testuser1@gmail.com")
    driver.find_element(By.NAME, "first_name").send_keys("ABC!@#")
    driver.find_element(By.NAME, "last_name").send_keys("ABC12345")
    driver.find_element(By.ID, "company").send_keys("123<>1223")
    driver.find_element(By.ID, "expertise").send_keys("ABCCC")

    # First Test: Password too short
    password_field = driver.find_element(By.ID, "password")
    password_confirm_field = driver.find_element(By.NAME, "password_confirmation")

    password_field.send_keys("1234")
    password_confirm_field.send_keys("123456")

    # Wait for the register button to be clickable and scroll into view
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-btn")))
    driver.execute_script("arguments[0].scrollIntoView(true);", register_button)

    # Wait for a moment to ensure the page finishes rendering
    time.sleep(1)  # Adjust this if necessary

    # Click the register button
    register_button.click()

    # Wait for error message to appear (password too short error)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback")))
    error_message = driver.find_element(By.CLASS_NAME, "invalid-feedback").text

    expected_error1 = "The password field must be at least 8 characters."
    assert expected_error1 in error_message, f"❌ Test Failed: Expected '{expected_error1}', but got '{error_message}'"
    print(f"✅ Test Success: '{expected_error1}' displayed.")

    # Re-fetch password fields after clicking submit
    password_field = driver.find_element(By.ID, "password")
    password_confirm_field = driver.find_element(By.NAME, "password_confirmation")

    password_field.send_keys("12345678")
    password_confirm_field.send_keys("123456789")

    # Re-fetch the register button after any DOM changes
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-btn")))
    driver.execute_script("arguments[0].scrollIntoView(true);", register_button)

    # Wait for a moment to ensure the page finishes rendering
    time.sleep(1)  # Adjust this if necessary

    # Click the register button again
    register_button.click()

    # Wait for error message to appear (password confirmation mismatch)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback")))
    error_message = driver.find_element(By.CLASS_NAME, "invalid-feedback").text

    expected_error2 = "The password field confirmation does not match."
    assert expected_error2 in error_message, f"❌ Test Failed: Expected '{expected_error2}', but got '{error_message}'"
    print(f"✅ Test Success: '{expected_error2}' displayed.")
