import json

person_string='{"name": "Faruk","languages":["Python","C","JavaScript","HTML","React.js","CSS","React Native"]}'
person_dict={"name": "Faruk","languages":["Python","C","JavaScript","HTML","React.js","CSS","React Native"]}

# JSON string to Dict
# result=json.loads(person_string)
# result=result["name"]
# result=result["languages"]
# print(result)

# with open("64person.json") as f:
#     data=json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["languages"])

# Dict to JSON string
# result=json.dumps(person_dict)
# print(result)
# print(type(result)) 

# with open("64person.json","w") as f:
#     json.dump(person_dict,f)

person_dict=json.loads(person_string)

result=json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)
