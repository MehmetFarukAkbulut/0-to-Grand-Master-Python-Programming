# Inheritance (Kalıtım):  Miras alma

# Person=> name,lastname,age,eat(),run(),drink()
# Student(Person),Teacher(Person)

# Animal => Dog(Animal),Cat(Animal)

class Person():
    def __init__(self,fname,lname) :
        self.firstName=fname
        self.lastName=lname
        print("Person Created.")

    def who_am_I(self):
        print("I am a person")
    def eat(self):
        print("I am eating.")
    
    
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print("Student Created.")

p1=Person("Faruk","Akbulut")
s1=Student("Rümeysa","Akbulut")
print(p1.firstName+" "+p1.lastName)
print(s1.firstName+" "+s1.lastName)

p1.who_am_I()
s1.who_am_I()
p1.eat()
s1.eat()