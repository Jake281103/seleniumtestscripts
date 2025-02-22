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

def test_password_reset_link(setup_browser):  
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/login")
    driver.set_window_size(1200, 1000)

    # Click the "Forgot Your Password?" link
    driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
    
    # Enter the email address for password reset
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("oothawmaung@gmail.com")
    
    # Click the send reset button
    driver.find_element(By.ID, "send-reset-btn").click()

    # Wait for success message to confirm the email was sent
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
    success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(f"Success Message: {success_message}")

