""" Python structure like properties using class """

class struct_sample():
    a = int()
    b = list()
    c = dict()

x = struct_sample
x.a = 1
x.b = [1,2,3,4]
x.c = {"color": "red"}

print(x.a, x.b, x.c)


