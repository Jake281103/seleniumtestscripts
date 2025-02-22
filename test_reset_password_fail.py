import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def setup_browser():  
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_register_success(setup_browser): 
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/login")
    driver.set_window_size(1200, 1000)

    # Wait for Register As Mentor link to apper and click 
    driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
    driver.find_element(By.ID, "email").send_keys("testerusers@gmail.com")

    driver.find_element(By.ID, "send-reset-btn").click()

    # Wait for error message to appear (password confirmation mismatch)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "invalid-feedback")))
    error_message = driver.find_element(By.CLASS_NAME, "invalid-feedback").text

    expected_error = "We can't find a user with that email address."
    assert expected_error in error_message, f"❌ Test Failed: Expected '{expected_error}', but got '{error_message}'"
    print(f"✅ Test Success: '{expected_error}' displayed.")


