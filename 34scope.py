# global scope

x= "global x"

def function():
    # local scope
    x="local x"
    print(x)
function()
print(x)


###############
#global
name="Faruk"

def changeName(new_name):
    #local
    global name
    name= new_name
    print(name)


changeName("Mehmet")
print(name)
####################
name="global string"

def greeting():
    # name="Faruk"
    def hello():
        # name="Mehmet"
        print("hello "+ name)

    hello()
greeting()
####################
x=50
def test():
    global x
    print(f"x: {x}")
    
    x=100
    print(f"changed x to {x}")
    
test()
print(x)
