cities = {
    'karachi':{
        'country':'pakistan',
        'population':21.20},
    'mumbai':{
        'country':'india',
        'population':18.41}}

for name, information in cities.items():

    print(name.title() + " - " + information['country'].title())
    print(str(information['population']) + " Million People")
    print()