import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

##########################################################################
# delete_one = tek bir kaydı siler , delete_many = birden fazla kaydı siler
print(40*"*"+" TEK KAYIT SİLME "+40*"*")
filter = {"name":"iphone 14"}
result = myCollection.delete_one(filter)
for r in myCollection.find(filter):
    print(r)
print("Silinen Kayıt Sayısı:",result.deleted_count)
print("\n")

for r in myCollection.find():
    print(r)
print("\n")
##########################################################################
filter = {"price":{"$gt":40000}}  # price değeri 40000'den büyük olan kayıtları siler
result = myCollection.delete_many(filter)   
for r in myCollection.find(filter):
     print(r)
print("Silinen Kayıt Sayısı:",result.deleted_count)

for r in myCollection.find():
    print(r)

##########################################################################
# Tüm kayıtları silme
# result = myCollection.delete_many({})