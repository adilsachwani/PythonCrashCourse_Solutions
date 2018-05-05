fav_numbers = {'adil':[23,2,38],
        'saba':[30,12,11],
        'naveed':[26],
        'rija':[31,15],
        'amna':[33,42]}

for name, numbers in fav_numbers.items():
    print(name.title() + "'s favourite number", end="")

    if len(numbers) ==  1:
        print(" is ", end="")
    else:
        print("s are ", end="")

    for i, number in enumerate(numbers):
        if i == len(numbers)-1:
            print(str(number) + ".", end="")
        else:
            print(str(number) + ", ", end="")

    print("")