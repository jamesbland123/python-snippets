""" Dictionary comprehension example """

dictionary = {"cat": 1, "dog": 3, "horse": 0}

dict_comp = {k:v for k,v in dictionary.items() if k == "dog"}

print(dict_comp)