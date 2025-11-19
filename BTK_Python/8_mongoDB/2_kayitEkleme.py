import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["BTK"]
myCollection = mydb["products"]

# print(mydb.list_collection_names())

# product = {
#     "name": "Samsung S20",
#     "price": 15000
# }

# result = myCollection.insert_one(product)
# print(result)
# print(type(result))

# products = [
#     {"name": "Samsung S21", "price": 20000},
#     {"name": "Samsung S22", "price": 25000},
#     {"name": "Samsung S23", "price": 30000},
#     {"name": "Samsung S24", "price": 35000},
#     {"name": "Samsung S25", "price": 40000},
#     {"name": "Samsung S26", "price": 45000},
# ]

products = [
     {"name": "Samsung S21", "price": 20000,"description":"Good Phone"},
     {"name": "Samsung S22", "price": 25000, "categories":["Phone", "Electronics"]}
 ]


result = myCollection.insert_many(products)
print(result)
print(type(result))