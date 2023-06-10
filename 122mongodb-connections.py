import pymongo
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]

print(myclient.list_database_names())