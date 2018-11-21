import requests
r = requests.get('https://jsonplaceholder.typicode.com/todos')
#Each record is indexed
#Get first index
print(r.json()[0])
print("************")
#Get last index
print(r.json()[len(r.json())-1])
print("************")
#The named section need to be indicated using the same notation, but instead of an index a name is provided
print (r.json()[0]["userId"])
print (r.json()[0]["id"])
print (r.json()[0]["title"])
print (r.json()[0]["completed"])