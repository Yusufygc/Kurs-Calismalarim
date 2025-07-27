from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("--dns-prefetch-disable")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")

service = Service(executable_path="D:\\1KodCalismalari\\Python-Calismalari\\BTK_Python\\5_bot_yazimi\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://github.com")
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # Arama kutusunu aç
    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-target='qbsearch-input.inputButtonText']"))
    )
    search_button.click()

    # Arama kutusuna yaz
    search_input = wait.until(
        EC.visibility_of_element_located((By.ID, "query-builder-test"))
    )
    search_input.send_keys("Python")
    search_input.send_keys(Keys.ENTER)

    print("🔍 Arama yapıldı, sonuçlar yükleniyor...")
    time.sleep(3)

    # "Repositories" sekmesine geç
    repos_tab = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="type=repositories"]'))
    )
    repos_tab.click()
    time.sleep(2)

    # Repo başlıklarını al
    repo_links = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search-title a"))
    )

    print("\n📄 İlk 5 Python Reposu:")
    for i, repo in enumerate(repo_links[:5], 1):
        name = repo.text.strip()
        link = repo.get_attribute("href")
        print(f"{i}. {name} - {link}")

    print("\n✅ Tamamlandı!")

except Exception as e:
    print("❌ Hata:", e)

driver.quit()