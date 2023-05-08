# # key - value

# #  41 => kocaeli  34=> istanbul

# sehirler=['kocaeli','istanbul','tekirdağ']
# plakalar=[41,34,59]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])
# print(plakalar[sehirler.index('tekirdağ')])

# # print(plakalar["kocaeli"])=>41
# # print(plakalar["istanbul"])=>34

# plakalar= { 'kocaeli': 41, 'istanbul': 34, 'tekirdağ':59}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])
# print(plakalar['tekirdağ'])
# plakalar['ankara']=6
# print(plakalar)

users={
    'farukakbulut':{
        'age':23,
        'roles': ['admin','user'],
        'email':'mefarukakbulut@gmail.com',
        'address':'istanbul',
        'phone':'1233123'
    },
    'rümeysaakbulut':{
        'age':25,
        'roles': ['user'],
        'email':'rümeysaakbulut@gmail.com',
        'address':'istanbul',
        'phone':'1233124'
    },
    'göksuoğur':{
        'age':21,
        'roles': ['user'],
        'email':'göksuogur@gmail.com',
        'address':'istanbul',
        'phone':'1233125'
    }
}


print(users['göksuoğur']['age'])
print(users['göksuoğur']['email'])
print(users['göksuoğur']['address'])
print(users['göksuoğur']['roles'][0])
print(users['farukakbulut']['age'])
print(users['farukakbulut']['email'])
print(users['farukakbulut']['address'])
print(users['farukakbulut']['roles'][0])