from selenium import webdriver
import time


driver = webdriver.Chrome()
url = "https://www.github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window() # Pencereyi tam ekran yapar
driver.save_screenshot("github_screenshot.png") # Ekran görüntüsü alır

url = "https://www.github.com/Yusufygc"
driver.get(url)
print("Sayfa Başlığı:", driver.title)

if "Yusufygc" in driver.title:
    driver.save_screenshot("yusufygc_screenshot.png")  # Ekran görüntüsü alır

time.sleep(2)
driver.back()  # Geri gider
time.sleep(2)
driver.close()