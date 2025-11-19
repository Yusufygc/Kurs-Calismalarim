import time
import undetected_chromedriver as uc # Yeni kütüphanemiz
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_tweets_stealth():
    # 1. Kullanıcıdan hisse kodunu al
    stock_code = input("Lütfen hisse senedi kodunu girin (Örn: THYAO): ").upper()
    search_term = f"${stock_code}" 

    # 2. Tarayıcı Ayarları (Undetected Chromedriver)
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--disable-popup-blocking")

    print("Sürücü hazırlanıyor... (Bu işlem ilk seferde birkaç saniye sürebilir)")
    # version_main parametresi Chrome sürümünü otomatik eşleştirir
    driver = uc.Chrome(options=options, use_subprocess=True) 

    try:
        # 3. X'e git
        print("X (Twitter) açılıyor...")
        driver.get("https://x.com/login")

        print("-" * 50)
        print("LÜTFEN DİKKAT: Artık 'Robot' uyarısı almadan giriş yapabilirsiniz.")
        print("60 saniye içinde giriş yapman bekleniyor...")
        print("-" * 50)
        
        # Manuel giriş için bekleme süresi
        time.sleep(60) 

        # 4. Arama Sayfasına Git
        print(f"{search_term} için canlı sonuçlar aranıyor...")
        search_url = f"https://x.com/search?q={search_term}&src=typed_query&f=live"
        driver.get(search_url)

        # Tweetlerin yüklenmesi için bekle
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))

        collected_tweets = set()
        
        # 5. Tweetleri Topla
        patience = 0 # Sonsuz döngüye girmemek için sabır sayacı
        while len(collected_tweets) < 10 and patience < 50:
            articles = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
            
            found_new = False
            for article in articles:
                try:
                    text_element = article.find_element(By.XPATH, './/div[@data-testid="tweetText"]')
                    tweet_text = text_element.text.replace("\n", " ")
                    
                    if tweet_text and tweet_text not in collected_tweets:
                        collected_tweets.add(tweet_text)
                        print(f"{len(collected_tweets)}. Tweet: {tweet_text[:100]}...")
                        found_new = True
                    
                    if len(collected_tweets) >= 10:
                        break
                except:
                    continue
            
            if not found_new:
                patience += 1
            
            # Sayfayı aşağı kaydır
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(3) # İnsan gibi davranmak için biraz daha uzun bekle

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    finally:
        print("-" * 50)
        print("İşlem tamamlandı.\n")
        
        print("TOPLANAN TWEETLER:\n")
        for i, tweet in enumerate(collected_tweets, 1):
            print(f"{i}) {tweet}\n")
            print("-" * 20)

        input("Tarayıcıyı kapatmak için Enter'a basın...")
        driver.quit()

if __name__ == "__main__":
    get_tweets_stealth()