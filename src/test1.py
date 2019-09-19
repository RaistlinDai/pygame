import json


with open('savedata01.json', 'r') as f:
    distros_dict = json.load(f)

characters = distros_dict["Characters"]
for temp_char in characters:
    for skill in temp_char['Skills']:
        for item in skill:
            print(skill[item])