import json

filename = 'fav_number.json'
prompt = "We don't know your favourite number. Kindly tell us then we we'll remmeber: "

try:
    with open(filename) as my_file:
        fav = json.load(my_file)

except FileNotFoundError:
    fav = input(prompt)
    with open(filename,'w') as my_file:
        json.dump(fav,my_file)

else:
    print("I know your favorite number! It is " + str(fav) + ".")