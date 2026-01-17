import pymongo
from bson.objectid import ObjectId

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

##########################################################################
filter = {"name":"Samsung S22"}
result = myCollection.find(filter) # Filtreye göre kayıtları getirir
for r in result:
    print(r) 
print("\n")   
##########################################################################

print(40*"*"+" ObjectId ile Kayıt Getirme "+40*"*")
filter = {"_id":ObjectId("691e2c30224f3be70e8a9538")}  # ObjectId ile kayıt getirme
result = myCollection.find_one(filter)
print(result,"\n")
##########################################################################
print(40*"*"+" Operatör ile Kayıt Getirme "+40*"*")
result = myCollection.find({
    "name":{"$in":["Samsung S21","Samsung S24"]} # name alanı Samsung S21 veya Samsung S24 olan kayıtları getirir
    })
for r in result:
    print(r)
print("\n")
##########################################################################
print(40*"*"+" Karşılaştırma Operatörleri ile Kayıt Getirme "+40*"*")
result = myCollection.find({
    "price":{"$gt":25000} # price alanı 25000'den büyük olan kayıtları getirir $gt: greater than $gte: greater than or equal
     # $lt: less than 
     # $lte: less than or equal 
     # $ne: not equal
    })
for r in result:
    print(r)
print("\n")
##########################################################################
print(40*"*"+" Regular Expression ile Kayıt Getirme "+40*"*")
result = myCollection.find({
    "name":{"$regex":"^Samsung S2"} # name alanı Samsung S2 ile başlayan kayıtları getirir
    })
for r in result:
    print(r)
print("\n")
##########################################################################