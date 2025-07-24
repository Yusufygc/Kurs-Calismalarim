import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
} # su anda bu header'i kullanmazsak, IMDB bize bir hata donduruyor. Bu header'i kullanarak IMDB'nin web sitesine girebiliyoruz. 
#cunku IMDB, botlardan korunmak icin bu header'i kontrol ediyor. headerin icindeki User-Agent, tarayicinin adini ve surumunu belirtir.

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste =soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li")

for film in liste:
  film_adi = film.find("h3", {"class": "ipc-title__text"}).text
  puan = film.find("span", {"class": "ipc-rating-star"}).text
  yil = film.find("span", {"class": "sc-29531a57-8 cxFOWT cli-title-metadata-item"}).text
  print(f"Film Adı    : {film_adi}")
  print(f"Film Puanı  : {puan}")
  print(f"Film Yılı   : {yil}")
  print("-" * 50) # her filmden sonra 50 tire yazdirir