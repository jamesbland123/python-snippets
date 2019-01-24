""" List comprehension examples """

d = "Every dog has his dog day"

# split string based on space
list_of_strings = [s for s in d.split()]

print(list_of_strings)

# split string on space with equality
match_list = [s for s in d.split() if s == "dog"]

print(match_list)

