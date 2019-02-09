import re

with open("file.txt") as f:
    
    for line in f:
        newline = line.rstrip()
        if re.search("jpg", newline):
            jpg = open("newfile.txt", "a+")
            jpg.write(newline)
            jpg.write("\n")
            jpg.close()    




