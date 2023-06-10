import pymongo
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]

# result= mycollection.find_one()
# for i in mycollection.find({},{"_id":0,"name":1,"price":1}):
for i in mycollection.find({},{"_id":0}):
    print(i)

# print(result)