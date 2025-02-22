import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="function")
def setup_browser():  
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_required_fields_one_by_one(setup_browser):  
    driver = setup_browser
    driver.get("https://intern-talks.nbgsoftware.com/")
    driver.set_window_size(1200, 1000)

    # Wait for Register As Mentor link to appear and click it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register As Mentor"))).click()

    # First field: email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_field.click()
    email_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: email_field.get_attribute("validationMessage") != "")
    validation_message = email_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for email"
    print(f"✅ Test Success: Validation message displayed for email")
    email_field.send_keys("example@gmail.com")

    # Second field: first_name
    first_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "first_name")))
    first_name_field.click()
    first_name_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: first_name_field.get_attribute("validationMessage") != "")
    validation_message = first_name_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for first_name"
    print(f"✅ Test Success: Validation message displayed for first_name")
    first_name_field.send_keys("John")

    # Third field: last_name
    last_name_field = wait.until(EC.visibility_of_element_located((By.NAME, "last_name")))
    last_name_field.click()
    last_name_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: last_name_field.get_attribute("validationMessage") != "")
    validation_message = last_name_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for last_name"
    print(f"✅ Test Success: Validation message displayed for last_name")
    last_name_field.send_keys("Doe")

    # Fourth field: company
    company_field = wait.until(EC.visibility_of_element_located((By.ID, "company")))

    # Scroll the company field into view before clicking
    driver.execute_script("arguments[0].scrollIntoView(true);", company_field)

    # Wait for the element to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(company_field))
    
    company_field.click()
    company_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: company_field.get_attribute("validationMessage") != "")
    validation_message = company_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for company"
    print(f"✅ Test Success: Validation message displayed for company")
    company_field.send_keys("Tech Corp")

    # Fifth field: expertise
    expertise_field = wait.until(EC.visibility_of_element_located((By.ID, "expertise")))
    expertise_field.click()
    expertise_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: expertise_field.get_attribute("validationMessage") != "")
    validation_message = expertise_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for expertise"
    print(f"✅ Test Success: Validation message displayed for expertise")
    expertise_field.send_keys("Software Development")

    # Sixth field: password
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.click()
    password_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: password_field.get_attribute("validationMessage") != "")
    validation_message = password_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for password"
    print(f"✅ Test Success: Validation message displayed for password")
    password_field.send_keys("Password123")

    # Seventh field: password_confirmation
    password_confirmation_field = wait.until(EC.visibility_of_element_located((By.NAME, "password_confirmation")))
    password_confirmation_field.click()
    password_confirmation_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(lambda d: password_confirmation_field.get_attribute("validationMessage") != "")
    validation_message = password_confirmation_field.get_attribute("validationMessage")
    expected_message = "Please fill out this field."
    assert validation_message == expected_message, f"❌ Test Failed: Expected '{expected_message}' but got '{validation_message}' for password_confirmation"
    print(f"✅ Test Success: Validation message displayed for password_confirmation")
    password_confirmation_field.send_keys("Password123")

    print("✅ All required fields tested and filled successfully.")
