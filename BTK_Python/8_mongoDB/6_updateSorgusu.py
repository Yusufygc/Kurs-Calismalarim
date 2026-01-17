import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

##########################################################################
# update_one = tek bir kaydı günceller , update_many = birden fazla kaydı günceller
print(40*"*"+" TEK KAYIT GÜNCELLEME "+40*"*")
filter = {"name":"Samsung S22"}
newValues = {"$set":{"price":27000}}  # $set ile belirtilen alanları günceller
result = myCollection.update_one(filter,newValues)
for r in myCollection.find(filter):
    print(r)
print("Güncellenen Kayıt Sayısı:",result.modified_count)
print("\n")
##########################################################################
filter = {"name":"Samsung S22"}
newValues = {"$set":{"name":"iphone 14","price":32000,"description":"Apple Phone"}}  # $set ile belirtilen alanları günceller
result = myCollection.update_one(filter,newValues)
for r in myCollection.find(filter):
    print(r)
print("Güncellenen Kayıt Sayısı:",result.modified_count)
##########################################################################

print(40*"*"+" GÜNCELLENMİŞ KAYITLAR "+40*"*")
guncel_kayitlar = myCollection.find()
for kayit in guncel_kayitlar:
    print(kayit)