from collections import defaultdict

fruits = ["apple", "pear", "orange", "apple", "orange"]

count = defaultdict(int)

for i in fruits:
    count[i] += 1


dups = {k:v for k,v in count.items() if v >= 2}

print(dups)


