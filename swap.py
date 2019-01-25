""" Python swap example """

a = 1
b = 2
print(a, b)

def swap(i, j):
    i, j = j, i
    return i, j

a, b = swap(a, b)
print(a, b)
