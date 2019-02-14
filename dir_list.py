""" List directory and iterate files """
import os

# find all files that end with .py 
for root, dirs, files in os.walk("."):  
    for filename in files:
        if str(filename).endswith("py"):
            print(filename)

print("{}".format("#"*20))

# find files in current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)

    