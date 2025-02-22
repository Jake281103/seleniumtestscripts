Selenium Test Scripts
This repository contains a collection of Selenium test scripts written in Python using the pytest framework for testing various user interactions on a web application. The scripts mainly focus on the registration, login, and profile management functionalities, ensuring that the application works as expected.

Table of Contents
 - Installation
 - Usage
 - Test Scenarios
 - Contributing

Installation
  To use the Selenium test scripts, follow the steps below:

  Clone the repository: git clone https://github.com/Jake281103/seleniumtestscripts.git
  Install the required dependencies: pip install -r requirements.txt
  
  Ensure you have Google Chrome installed and the appropriate ChromeDriver matching your Chrome version.
  Place the chromedriver in /usr/bin/ or adjust the path in the scripts as necessary.

Usage
 To run the tests, you can use the pytest framework. You can run all tests using: pytest
  
  Example Test Run
    pytest test009.py
    
Test Scenarios
   The repository contains the following test scenarios:
  1. Registration Success (test009.py)
      Test that a user can successfully request a password reset and receive the correct success message.

  2. Registration Failure (test001.py & test002.py)
       Test for various registration failures, such as invalid email formats and password mismatches.

  3. Profile Image Upload (test005.py)
       Test for uploading a profile image and ensure the image updates correctly.
     
  4. Required Fields Validation (test003.py)
       Test that all required fields on the registration form trigger validation when left empty.
     
  5. Login Failure (test006.py)
       Test login failure due to invalid credentials.
     
  6. Successful Registration (test007.py & test004.py)
      Test that a user can successfully register and be redirected to the dashboard.
     
 Each test script is modular, focusing on specific application features and validations.

Contributing
   We welcome contributions to this repository! Please follow these steps to contribute:

   1. Fork the repository.
   2. Create a new branch (git checkout -b feature-branch).
   3. Make your changes.
   4. Commit your changes (git commit -am 'Add new feature').
   5. Push to the branch (git push origin feature-branch).
   6. Create a pull request.
