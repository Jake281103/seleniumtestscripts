import pytest
import os
import time
from datetime import datetime

# Directory to store logs
LOG_FILE = "test_results.log"

# Store the success and failure counts, and the lists of test names
success_tests = []
fail_tests = []

def log_message(message):
    """Log the message to the log file and print it."""
    with open(LOG_FILE, "a") as log_file:  # Open the log file in append mode
        log_file.write(message + "\n")
    print(message)

def run_tests(test_files):
    """Run the specified tests and log the results."""
    result = pytest.main(test_files)
    return result

def get_test_files():
    """Return a list of test files to be run."""
    return [
        'test_register_fail1.py',
        'test_register_fail2.py',
        'test_register_fail3.py',
        'test_register_success1.py',
        'test_register_success2.py',
        'test_login_fail.py',
        'test_login_success.py',
        'test_reset_password_fail.py',
        'test_reset_password_success.py'
    ]

def log_test_result(test_file, result_code, start_time):
    """Log the result of a single test file."""
    end_time = time.time()
    testing_time = round(end_time - start_time, 2)  # In seconds
    result = "Success" if result_code == 0 else "Failure"
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log success or failure without error messages
    log_message(f"{time_str} | {test_file} | {result} | Test Time: {testing_time}s")
    
    # Track success/failure counts and lists
    if result_code == 0:
        success_tests.append(test_file)
    else:
        fail_tests.append(test_file)

def pytest_runtest_makereport(item, call):
    """Hook to capture success/failure of tests without error messages."""
    if call.excinfo is not None:  # If the test failed
        log_test_result(item.nodeid, 1, time.time())  # Log failure without error message
    else:  # If the test passed
        log_test_result(item.nodeid, 0, time.time())

def main():
    total_start_time = time.time()
    log_message("Test Run Started.\n")

    print("Choose an option to run the tests:")
    print("1. Run all test scripts")
    print("2. Run a specific test script")
    print("3. Run a range of test scripts (e.g., 2-5)")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        log_message("Running all test scripts...")
        for test_file in get_test_files():
            log_message(f"Running {test_file}...")
            start_time = time.time()
            result = run_tests([test_file])
            log_test_result(test_file, result, start_time)

        total_end_time = time.time()
        total_testing_time = round(total_end_time - total_start_time, 2)
        log_message(f"Total Test Time: {total_testing_time}s")

    elif choice == "2":
        test_file = input("Enter the name of the test file to run (e.g., 'test001.py'): ").strip()
        if test_file in get_test_files():
            log_message(f"Running {test_file}...")
            start_time = time.time()
            result = run_tests([test_file])
            log_test_result(test_file, result, start_time)
        else:
            log_message(f"❌ Invalid test file: {test_file}")
    
    elif choice == "3":
        start = int(input("Enter the starting test number (e.g., 2): ").strip())
        end = int(input("Enter the ending test number (e.g., 5): ").strip())
        all_tests = get_test_files()
        if 1 <= start <= len(all_tests) and 1 <= end <= len(all_tests) and start <= end:
            selected_tests = all_tests[start-1:end]  # Adjusting to 0-based indexing
            log_message(f"Running tests from {selected_tests[0]} to {selected_tests[-1]}...")
            total_start_time = time.time()
            for test_file in selected_tests:
                log_message(f"Running {test_file}...")
                start_time = time.time()
                result = run_tests([test_file])
                log_test_result(test_file, result, start_time)

            total_end_time = time.time()
            total_testing_time = round(total_end_time - total_start_time, 2)
            log_message(f"Total Test Time: {total_testing_time}s")

        else:
            log_message(f"❌ Invalid range: {start}-{end}")
    
    else:
        log_message("❌ Invalid choice. Please select 1, 2, or 3.")

    # Final summary
    total_end_time = time.time()
    total_testing_time = round(total_end_time - total_start_time, 2)
    log_message(f"\nTest Run Completed. Total Time: {total_testing_time}s")
    
    # Log the summary counts and lists
    total_tests = len(success_tests) + len(fail_tests)
    success_count = len(success_tests)
    fail_count = len(fail_tests)
    
    log_message(f"\nTotal Tests Run: {total_tests}")
    log_message(f"Successful Tests: {success_count}")
    log_message(f"Failed Tests: {fail_count}")
    
    if success_count > 0:
        log_message("\nSuccessful Tests:")
        for test in success_tests:
            log_message(f"  - {test}")
    
    if fail_count > 0:
        log_message("\nFailed Tests:")
        for test in fail_tests:
            log_message(f"  - {test}")

if __name__ == "__main__":
    main()
