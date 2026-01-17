import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

print(40*"*"+" İLK KAYIT "+40*"*")
result = myCollection.find_one() # İlk kaydı getirir
print(result,"\n")

print(40*"*"+" TÜM KAYITLAR "+40*"*")
results = myCollection.find() # Tüm kayıtları getirir
for result in results:
    print(result,"\n")

print(40*"*"+" SEÇİLEN KAYITLAR "+40*"*")
selected_results = myCollection.find({},{"_id":0,"name":1,"price":1}) # Seçilen alanları getirir
# sadece id 0 yaparsak id hariç tüm alanları getirir
for result in selected_results:
    print(result)