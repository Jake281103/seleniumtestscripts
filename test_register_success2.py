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

def test_register_success(setup_browser): 
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/")
    driver.set_window_size(1200, 1000)

    # Wait for Register As Mentor link to appear and click it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register As Mentor"))).click()

    # Locate the profile image preview element
    profile_preview = driver.find_element(By.ID, "previewImg")
    initial_img_src = profile_preview.get_attribute("src")
    print(f"Initial profile image source: {initial_img_src}")

    # Set the file path (Ensure the file exists on your system)
    file_path = "/home/thaw-maung-oo/Desktop/tmo.jpg"  # Replace with the path to an actual image file on your machine
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} was not found!")

    # Send the file to the hidden file input field
    file_input = driver.find_element(By.ID, "upload_profile")
    file_input.send_keys(file_path)

    # Wait for the image to be updated (You can check the profile image src again)
    time.sleep(3)  # Give it time to process the image

    # Verify the image source has changed
    updated_img_src = profile_preview.get_attribute("src")
    assert updated_img_src != initial_img_src, "❌ Test Failed: Profile image did not update after upload."
    print("✅ Test Success: Profile image uploaded and updated successfully.")

    # Fill out the form fields with valid data
    driver.find_element(By.ID, "email").send_keys("oothawmaung123@gmail.com")
    driver.find_element(By.NAME, "first_name").send_keys("Mg Mg")
    driver.find_element(By.NAME, "last_name").send_keys("Oo")
    driver.find_element(By.ID, "company").send_keys("SST")
    driver.find_element(By.ID, "expertise").send_keys("Network Engineer")
    driver.find_element(By.ID, "password").send_keys("123456789")
    driver.find_element(By.NAME, "password_confirmation").send_keys("123456789")

    # Wait for the register button to be clickable
    register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-btn")))

    # Scroll the button into view to avoid interception
    driver.execute_script("arguments[0].scrollIntoView(true);", register_button)

    # Wait for a moment to ensure the page finishes rendering
    time.sleep(3)  # Adjust this if necessary

    # Click the register button
    register_button.click()

    # Wait for the page to navigate to the expected dashboard URL
    wait.until(EC.url_to_be("https://intern-talks.nbgsoftware.com/intern/list"))
    assert driver.current_url == "https://intern-talks.nbgsoftware.com/intern/list", \
        f"Expected URL to be the dashboard, but got {driver.current_url}"
    print("✅ Test Success: Registration successful and redirected to the dashboard.")


