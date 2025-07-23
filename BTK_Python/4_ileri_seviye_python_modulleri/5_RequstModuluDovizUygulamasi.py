import requests
import json

api_key = "1c486ed1ee6a52dbcfe04d94"
api_url =  f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

islem_yapilan_doviz = input("İşlem yapılan döviz birimini giriniz (örn: USD): ").upper()
islem_sonucu_alinan_doviz = input("İşlem sonucu alınan döviz birimini giriniz (örn: EUR): ").upper()
miktar =input(f'Ne kadar {islem_yapilan_doviz} dönüştürmek istiyorsunuz?: ')

response = requests.get(api_url + islem_yapilan_doviz)
response_json = json.loads(response.text)
#print(response_json['conversion_rates'][islem_sonucu_alinan_doviz])

print(f"{islem_yapilan_doviz} -> {islem_sonucu_alinan_doviz} dönüşüm oranı: {response_json['conversion_rates'][islem_sonucu_alinan_doviz]}")
print(f"{miktar} {islem_yapilan_doviz} = {float(miktar) * response_json['conversion_rates'][islem_sonucu_alinan_doviz]} {islem_sonucu_alinan_doviz}")