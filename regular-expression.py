import re

phrase = "the quick brown fox jumped over the lazy dog"
patterns = ['quick', 'fox']

for pattern in patterns:
    match = re.search(pattern, phrase)

    if match:
        print(match.group(0))
    else:
        print("no match found")    



