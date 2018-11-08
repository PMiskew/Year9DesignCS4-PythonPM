import json
from pprint import pprint
#IMPORTANT: A JSON file is not a database!
#A JSON file is a data interchange document
with open('data.json') as f:
    data = json.load(f)

print(data) #prints everything
print(data["maps"][0]["id"])
print(data["masks"]["id"])
print(data["om_points"])