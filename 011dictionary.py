# # key - value

# #  41 => Kocaeli  34=> Istanbul 

# sehirler=['Kocaeli','Istanbul','Tekirdağ']
# plakalar=[41,34,59]

# print(plakalar[sehirler.index('Kocaeli')])
# print(plakalar[sehirler.index('Istanbul')])
# print(plakalar[sehirler.index('Tekirdağ')])

# # print(plakalar["Kocaeli"])=>41
# # print(plakalar["Istanbul"])=>34

# plakalar= { 'Kocaeli': 41, 'Istanbul': 34, 'Tekirdağ':59}
# print(plakalar['kocaeli'])
# print(plakalar['Istanbul'])
# print(plakalar['Tekirdağ'])
# plakalar['Ankara']=6
# print(plakalar)

users={
    'farukakbulut':{
        'age':23,
        'roles': ['admin','user'],
        'email':'mefarukakbulut@gmail.com',
        'address':'Istanbul',
        'phone':'1233123'
    },
    'rümeysaakbulut':{
        'age':25,
        'roles': ['user'],
        'email':'rümeysaakbulut@gmail.com',
        'address':'Istanbul',
        'phone':'1233124'
    },
    'fatihakbulut':{
        'age':32,
        'roles': ['user'],
        'email':'fatihakbulut@gmail.com',
        'address':'Eskişehir',
        'phone':'1233125'
    }
}


print(users['fatihakbulut']['age'])
print(users['fatihakbulut']['email'])
print(users['fatihakbulut']['address'])
print(users['fatihakbulut']['roles'][0])
print(users['farukakbulut']['age'])
print(users['farukakbulut']['email'])
print(users['farukakbulut']['address'])
print(users['farukakbulut']['roles'][0])
