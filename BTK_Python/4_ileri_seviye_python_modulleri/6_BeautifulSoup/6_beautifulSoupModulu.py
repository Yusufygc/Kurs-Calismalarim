html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 id="header">BeautifulSoup ile HTML Parse Etme</h1>
    <div class="content">
            <h2>Programlama</h2>
        
        <ul>
            <li>BeautifulSoup Nedir?</li>
            <li>Kurulum</li>
            <li>Temel Kullanım</li>
            <li>Örnek Uygulama</li>
        </ul>
    </div>

        <div class="content2">
            <h2>Moduller</h2>
        
        <ul>
            <li>BeautifulSoup Nedir?</li>
            <li>Kurulum</li>
            <li>Temel Kullanım</li>
            <li>Örnek Uygulama</li>
        </ul>
    </div>

        <div class="content3">
            <h2>Python Web Scraping</h2>

        <ul>
            <li>BeautifulSoup Nedir?</li>
            <li>Kurulum</li>
            <li>Temel Kullanım</li>
            <li>Örnek Uygulama</li>
        </ul>
    </div>
    <img src="StockMarketTrend.jpeg" alt="trend is your friend" width="500" height="300">
</body>
</html>

"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser") #html_doc degiskeni icindeki html kodunu parse eder

results = soup.prettify() #html dokumanini daha okunabilir hale getirir
results = soup.title # html dokumaninin basligini alir
results = soup.find_all("h2") # html dokumanindaki tum h2 etiketlerini bulur
results = soup.find_all("h2")[2] # sadece 3. h2 etiketini alir
#print(results)

content = soup.title.string # title etiketinin icerigini alir
#print(content)

result = soup.div # class'i content olan ilk div etiketini bulur
result = soup.find_all("div", class_="content2") # class'i content2 olan tum div etiketlerini bulur
result = soup.find_all("div", class_="content3")[0].h2.string # class'i content3 olan ilk div etiketinin icindeki h2 etiketinin icerigini alir
# print(result)

result1=soup.div.findChildren() # class'i content olan ilk div etiketinin icindeki tum etiketleri bulur
print(result1)
