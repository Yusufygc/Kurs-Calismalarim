
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service

username =''
password = ''
class Instagram:
    def __init__(self, username, password):
        self.username = username    
        self.password = password
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def sign_in(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))

        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/{self.username}')]")))

    def get_all_followers(self):
        # Takipçi sayısını al
        self.driver.get(f'https://www.instagram.com/{self.username}/')
        time.sleep(3)
        
        try:
            followers_count_element = self.driver.find_element(
                By.XPATH, "//a[contains(@href,'followers')]/span"
            )
            followers_count = followers_count_element.get_attribute("title") or followers_count_element.text
            print(f"📊 Toplam Takipçi Sayısı: {followers_count}")
        except:
            print("❌ Takipçi sayısı alınamadı!")
            followers_count = "Bilinmiyor"

        # Takipçi listesini aç
        self.driver.find_element(By.XPATH, "//a[contains(@href,'followers')]").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))

        print("✅ Takipçi listesi açıldı. Tüm takipçiler yükleniyor...")

        # Scroll kutusunu bul
        scroll_box = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='dialog']//div[contains(@class, 'isgrP') or contains(@style, 'overflow')]")
            )
        )

        # Scroll yaparak tüm takipçileri yükle
        last_height = 0
        same_height_count = 0
        max_attempts = 100  # Daha fazla scroll yapmak için
        followers = set()  # Tekrar edenleri engellemek için

        while same_height_count < 5 and max_attempts > 0:
            # Scroll işlemi
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(1.5)  # Yüklenmesi için bekle
            
            # Yüklenen takipçileri al
            new_followers = self.driver.find_elements(
                By.XPATH, "//div[@role='dialog']//a[contains(@href, '/') and not(contains(@href, '/followers'))]"
            )
            
            # Kullanıcı adlarını ekle
            for follower in new_followers:
                username = follower.text.strip()
                if not username:
                    href = follower.get_attribute("href")
                    if href:
                        username = href.rstrip("/").split("/")[-1]
                if username:
                    followers.add(username)
            
            # Scroll yüksekliğini kontrol et
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_box)
            if new_height == last_height:
                same_height_count += 1
            else:
                same_height_count = 0
            last_height = new_height
            max_attempts -= 1

        print(f"\n👥 Toplam {len(followers)}/{followers_count} Takipçi Bulundu:")
        for i, username in enumerate(sorted(followers), 1):
            print(f"{i}. {username}")

        return followers

# Kullanım
username = "kullanici_adiniz"  # Değiştir
password = "sifreniz"          # Değiştir

insta = Instagram(username, password)
insta.sign_in()
time.sleep(3)
insta.get_all_followers()
time.sleep(30)  # Sonucu görmek için bekle