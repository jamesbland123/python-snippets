""" Json loads and dumps """
import json

# dump Dict to json
x = {"Name": "Peter", "Age": 35, "Occupation": "Engineer"}
print(json.dumps(x))

# load json to dictionary
y = '{"Name": "Peter", "Age": 35, "Occupation": "Engineer"}'
json_to_dict = json.loads(y)

for k,v in json_to_dict.items():
    print('Key: {} Value: {}'.format(k,v))

    