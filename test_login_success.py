import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


@pytest.fixture(scope="function")
def setup_browser():  
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login_success(setup_browser): 
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/")
    driver.set_window_size(1200, 1000)

    # Wait for Register As Mentor link to appear and click it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register As Mentor"))).click()

    # Wait until the "Already have an account?" link is visible and clickable
    signin_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Already have an account?")))

    # Scroll the button into view to avoid interception
    driver.execute_script("arguments[0].scrollIntoView(true);", signin_button)

    # Ensure the element is visible and not covered by another element
    wait.until(EC.visibility_of(signin_button))

    # Wait for a moment to ensure the page finishes rendering
    time.sleep(3)  # Adjust this if necessary

    # Click the register button
    signin_button.click()

    # Fill out the form fields with valid data
    driver.find_element(By.ID, "email").send_keys("oothawmaung12@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456789")
    
    driver.find_element(By.ID, "login-btn").click()

     # Wait for the page to navigate to the expected dashboard URL
    wait.until(EC.url_to_be("https://intern-talks.nbgsoftware.com/intern/list"))
    assert driver.current_url == "https://intern-talks.nbgsoftware.com/intern/list", \
        f"Expected URL to be the dashboard, but got {driver.current_url}"
    print("✅ Test Success: Registration successful and redirected to the dashboard.")







