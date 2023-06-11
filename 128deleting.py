import pymongo
from bson.objectid import ObjectId
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]


for i in mycollection.find():
    print(i)
print("*"*50)

# mycollection.delete_one({"name":"Iphone 8"})
# mycollection.delete_many({"name":{"$regex":"^S"}})
result= mycollection.delete_many({})
print(f"{result.deleted_count} adet kayıt silindi.")

for i in mycollection.find():
    print(i)