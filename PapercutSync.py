from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your WebDriver if it's not in your system PATH
driver_path = 'path/to/chromedriver'

# Initialize the WebDriver
driver = webdriver.Chrome(driver_path)

try:
    # Navigate to the page
    driver.get('http://10.1.10.107:9191/app?service=page/OptionsUserSync')

    # Wait for the page to load and the checkbox to be present
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.presence_of_element_located((By.ID, 'delete-users-on-sync')))

    # Check the checkbox
    if not checkbox.is_selected():
        checkbox.click()

    # Wait for the "Synchronize Now" button to be present
    sync_button = wait.until(EC.presence_of_element_located((By.NAME, '$Submit$10')))

    # Click the "Synchronize Now" button
    sync_button.click()

    # Handle the confirmation dialog if it appears
    try:
        alert = wait.until(EC.alert_is_present())
        alert.accept()
    except:
        pass  # No alert appeared

    print("Synchronization initiated successfully.")

finally:
    # Close the WebDriver
    driver.quit()
