sandwich_orders = ['pastrami','club','bbq','pastrami','egg','special','pastrami']
finisjed_sandwiches = []

print("We have run out of Pastrami Sandwiches\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("We have made for " + current_sandwich.title() + " sandwich.")
    finisjed_sandwiches.append(current_sandwich)

print()

for sandwich in finisjed_sandwiches:
    print(sandwich.title() + " sandwich is read.")