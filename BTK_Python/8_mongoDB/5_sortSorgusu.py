import pymongo
from bson.objectid import ObjectId

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

result = myCollection.find().sort("name")  # name alanına göre artan sırada sıralar 
# sort("name",1) ile aynı anlama gelir artan şekilde sıralar
# result = myCollection.find().sort("name",-1)  # name alanına göre azalan sırada sıralar
for r in result:
    print(r)

print(40*"*"+" FARKLI KOLONLAR İLE SIRALAMA "+40*"*")
# isme göre sıralama yap ve aynı isimli kayıtlar için fiyata göre azalan sırada sırala
result = myCollection.find().sort([("name",1),("price",-1)])  # name alanına göre artan, price alanına göre azalan sırada sıralar
for r in result:
    print(r)