sandwich_orders = ['club','bbq','egg','special']
finisjed_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("We have made for " + current_sandwich.title() + " sandwich.")
    finisjed_sandwiches.append(current_sandwich)

print()

for sandwich in finisjed_sandwiches:
    print(sandwich.title() + " sandwich is read.")