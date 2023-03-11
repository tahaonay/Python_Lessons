import json

# dict

person_str = '{"name":"taha","dil":["python","c++"]}'


# JSON string to dict
result = json.loads(person_str)

# print(result)
# print(result["name"])

"""
with open("kisiler.json") as d:
    data = json.load(d)
    print(data)

"""
#string to JSON

with open("kisiler.json","w") as d:
    json.dump(person_str,d)

