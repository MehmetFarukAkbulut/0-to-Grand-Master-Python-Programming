import pymongo
from bson.objectid import ObjectId
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]

# result=mycollection.find().sort("name")#default=asc
# result=mycollection.find().sort("name",1)#asc
result=mycollection.find().sort("name",-1)#desc
result=mycollection.find().sort("price",-1)#desc
result=mycollection.find().sort([("name",1),("price",-1)])


for i in result:
    print(i)