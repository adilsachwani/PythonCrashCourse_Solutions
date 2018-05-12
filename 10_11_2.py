import json

filename = 'fav_number.json'

try:
    with open(filename) as my_file:
        fav = json.load(my_file)
except FileNotFoundError:
    pass
else:
    print("I know your favorite number! It is " + str(fav) + ".")