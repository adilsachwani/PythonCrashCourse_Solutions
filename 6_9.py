favourite_places = {'adil' : ['dubai','malaysia','singapore'],
                    'saba' : ['australia'],
                    'naveed' : ['india','newzealand'],
                    'rija' : ['pakistan']}

for name, places in favourite_places.items():
    print(name.title() + "'s favourite place", end="")

    if len(places) ==  1:
        print(" is ", end="")
    else:
        print("s are ", end="")

    for i, place in enumerate(places):
        if i == len(places)-1:
            print(place.title() + ".", end="")
        else:
            print(place.title() + ", ", end="")

    print("")