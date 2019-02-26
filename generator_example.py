""" Generator Example """

test_gen = (x for x in range(10))

for i in test_gen:
    print(i)


def getNum(num):
    while num > 0:
        yield num
        num -= 1

val = getNum(10)

print("*" * 10)
print(next(val))
print(next(val))
