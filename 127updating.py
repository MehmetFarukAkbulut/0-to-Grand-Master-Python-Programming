import pymongo
from bson.objectid import ObjectId
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]


for i in mycollection.find():
    print(i)

# update_one
# mycollection.update_one(
#     {"name":"Samsung S5"},
#     {"$set":{
#         "name":"Iphone 6","price":10000}}
# )
# update_many
# mycollection.update_many(
#     {"name":"Samsung S7"},
#     {"$set":{
#         "name":"Iphone 8","price":12000}}
# )
query={"name":"Samsung S7"}
newvalues={"$set":{
        "name":"Iphone 8",
        "price":12000
        }}
result=mycollection.update_many(query,newvalues)
print(f"{result.modified_count} adet kayıt güncellendi.")

for i in mycollection.find():
    print(i)
