""" Recursion examples """

# Fibonacci 
def fib(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1

    else:
        return fib(n-1) + fib(n-2)

print(fib(5))  # sequence is 1 1 2 3 5 

# Fibonacci using iterator
def fiberator():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

num = 10
j = 1
for i in fiberator():
    if j > num:
        break
    j += 1
    print(i)


# Towers of Hanoi
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(4,"A","B","C")