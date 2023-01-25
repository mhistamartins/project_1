import json

# opening JSON file
with open('min_signals.json', 'r') as openfile:
#Reading from json file
    json_object = json.load(openfile)
print(json_object)
print(type(json_object))

