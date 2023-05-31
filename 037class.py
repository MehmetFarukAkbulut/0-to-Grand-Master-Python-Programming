# class
class Person:
    # class attributes
    address= "no information"
    # constructor
    def __init__(self,name,year):
        # object attributes
        self.name= name
        self.year= year
    # methods

# if a>10:
#     pass

# object, instance
p1=Person(name="Faruk",year=2000)
p2=Person(name="Fatih",year=1991)

# updating
p1.name="Rümeysa"
p1.year= 1998
p1.address="İstanbul"
p2.name="Faruk"
p2.year= 2000
p2.address="İstanbul"

# accesing object attributes
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)