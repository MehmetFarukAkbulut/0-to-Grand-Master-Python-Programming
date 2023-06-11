import pymongo
from bson.objectid import ObjectId
mng="mongodb+srv://mfarukakbulut23:mfa23mfa23@cluster0.artnni6.mongodb.net/node-app?retryWrites=true&w=majority"
# myclient= pymongo.MongoClient("mongodb://localhost:27017")
myclient= pymongo.MongoClient(mng)

mydb=myclient["node-app"]
mycollection=mydb["products"]
# result= mycollection.find_one({"name": "Samsung S5"})
# result= mycollection.find_one({"_id":ObjectId("64847d6de6c2375219002647")})
# print(result)


# result= mycollection.find({"name": "Samsung S6"})


# result= mycollection.find({
#     "name": {
#              #"$in": ["Samsung S5","Samsung S6"]#olan kayıtlar
#              "$nin": ["Samsung S5","Samsung S6"]#olmayan kayıtlar
#             }

# })

# result=mycollection.find({
#     "price": {
#         # "$gt":6000#büyük olanlar
#         # "$gte":6000#büyük eşit olanlar
#         # "$lte":6000#küçük eşit olanlar
#         # "$lt":6000#küçük olanlar
#         # "$ne":6000# eşit olmayanlar
#         "$eq":6000# eşit olanlar
#     } 
# })
# result=mycollection.find({"$or":[{"price":{"$lt":6000}},{"price":10000}]})
# result=mycollection.find({"$nor":[{"price":{"$lt":6000}},{"price":10000}]})
# result=mycollection.find({"$and":[{"price":{"$gt":6000}},{"price":10000}]})

result=mycollection.find({"name":{"$regex":"^S"}})

for i in result:
    print(i) 