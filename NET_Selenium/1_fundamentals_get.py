"""import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.geeksforgeeks.org/python/navigating-links-using-get-method-selenium-python/"
driver.get(url)
time.sleep(2)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser and open Google
drv = webdriver.Chrome()
drv.get("https://www.google.com//")

# Search "GeeksforGeeks"
box = drv.find_element(By.NAME, "q")
box.send_keys("GeeksforGeeks", Keys.RETURN)

# Wait and close browser
time.sleep(5)
drv.quit()