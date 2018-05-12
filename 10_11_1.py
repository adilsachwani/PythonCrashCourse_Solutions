import json

prompt = 'Enter your favourite number: '
filename = 'fav_number.json'

fav = input(prompt)

with open(filename,'w') as my_file:
    json.dump(fav,my_file)