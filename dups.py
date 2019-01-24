""" A an example of using defaultdict to find 
    duplicates in a list """

from collections import defaultdict


fruits = ["apple", "pear", "orange", "apple", "orange"]

count = defaultdict(int)

for i in fruits:
    count[i] += 1


dups = {k:v for k,v in count.items() if v >= 2}

print(dups)

# Alternative to dictionary comprehension

for k in list(count):
    if count[k] >= 2:
        print("Key: {} has count {}".format(k, count[k]))


