def make_sandwich(*ingredients):
    print("Sandiwich contains: ")
    for ingredient in ingredients:
        print(ingredient.title())

make_sandwich("Cucumber","Cheese","Butter")
print("")
make_sandwich("Olives","tomatoes","cucumber","Chicken")