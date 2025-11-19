# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys
from selenium.webdriver.support.ui import WebDriverWait  # To wait for elements
from selenium.webdriver.support import expected_conditions as EC  # For expected conditions
import time

# Create a webdriver object. Here we use Firefox, but you can choose other browsers like Chrome, Edge, etc.
driver = webdriver.Chrome()

# Navigate to the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Maximize the browser window
driver.maximize_window()

# Wait for 3 seconds to ensure the page is loaded
time.sleep(3)

# Handle iframe if one exists (e.g., an overlay)
iframe_element = driver.find_element(By.XPATH, "//iframe[contains(@src,'accounts.google.com')]")
driver.switch_to.frame(iframe_element)

# Close the overlay (e.g., Google sign-in iframe)
closeele = driver.find_element(By.XPATH, "//*[@id='close']")
closeele.click()

# Wait for the iframe action to complete
time.sleep(3)

# Switch back to the main content
driver.switch_to.default_content()

# Locate the search icon element using XPath
searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")

# Wait for 3 seconds before interacting with the search input
time.sleep(3)

# Locate the input field for search text using XPath
enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

# Enter the search query "Data Structure" into the input field
enterText.send_keys("Data Structure")

# Send the RETURN key to submit the search query
enterText.send_keys(Keys.RETURN)