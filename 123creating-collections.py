import pymongo
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]
# print(mydb.list_collection_names())

# product={"name": "Samsung S5", "price":5000}

# result=mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)


productList=[
    {"name": "Samsung S6", "price":6000,"description":"iyi telefon"},
    {"name": "Samsung S7", "price":7000,"categories":["telefon","elektronik"]}
    ]
result= mycollection.insert_many(productList)
print(result.inserted_ids)