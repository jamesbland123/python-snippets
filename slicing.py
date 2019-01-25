""" Slicing examples """

a = list()

for i in range(1,11):
    a.append(i)

# 1 through 5
print(a[0:5])

# Every other
print(a[::2])

# last 3
print(a[-3:])

# all but last 3
print(a[:-3])
