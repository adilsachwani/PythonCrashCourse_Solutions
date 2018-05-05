prompt1 = "Please enter your name: "
prompt2 = "If you could visit one place in the world, where would you go? "
dream_place = {}
active = True

while active:
    name = input(prompt1)
    place = input(prompt2)

    dream_place[name] = place

    print()
    another = input("Other user? (y/n) ")
    if another == 'n':
        active = False

for name, place in dream_place.items():
    print(name.title() + "'s favourite place is " + place.title() + ".")
