tommy = {'kind':'dog',
         'owner' : 'adil'}

addy = {'kind':'parrot',
        'owner' : 'saba'}

baby = {'kind':'cat',
        'owner' : 'naveed'}

pets = [tommy,addy,baby]

for pet in pets:
    print("This " + pet['kind'].title() + " is owned by " + pet['owner'].title() )