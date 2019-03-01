""" var scoping """

# Global Scope
name = "John"
num = int()

# Local Scope
def changeName(new_name):
    name = new_name # Does not set new global name
    print(name)

def changeNameGlobal(new_name):
    global name
    name = new_name
    print(name)

print(name)                 # John
changeName("Peter")         # Peter
print(name)                 # John
changeNameGlobal("Paul")    # Paul
print(name)                 # Paul

## Using nonlocal binds one level up
x = "a"
def outer():
    x = "b"
    def inner():
        nonlocal x          # binds to outer x
        x = "c"             # assigns c to outer x
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)