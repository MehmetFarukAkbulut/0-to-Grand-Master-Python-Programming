# def changeName(n):
#     n="faruk"
# name="mehmet"
# changeName(name)
# print(name)

# def change(n):
#     n[0]="istanbul"
    
    
# sehirler=["ankara","izmir"]
# # change(sehirler)

# change(sehirler[:])#slicing

# # n[0]="istanbul"

# print(sehirler)
# def add(a,b,c=0):
#     return sum((a,b,c))
# def add(*params):
#     print(params)
#     return sum((params))
def add(*params):
    print(type(params))

    sum=0
    for n in params:
        sum+=n
    return sum
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))

def displayUser(**args):
    print(type(args))
    for key,value in args.items():
        print(f"{key} is {value}")

displayUser(name="Umut",age=4, city="tekirdağ")
displayUser(name="Fatih",age=32, city="eskişehir",phone="123123123")
displayUser(name="Faruk",age=23, city="istanbul",phone="456456456",email="fdafadsfdaf")

def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50,key1="value 1",key2="value 2")