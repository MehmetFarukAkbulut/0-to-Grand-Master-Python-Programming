numbers=[1,2,3,4,5]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

for num in numbers:
    print(num)
names=["faruk","rümeysa","fatih"]

for name in names:
    print(f"my name is {name}")    

name=" Faruk Akbulut"
for n in name:
    print(n)

tuple=[(1,2),(3,4,5),(5,6),(7,8)]

for a,*b in tuple:
    print(a,b)
    
d= {"k1":1, "k2":2,"k3":3}

for key,value in d.items():
    print(key,value)
