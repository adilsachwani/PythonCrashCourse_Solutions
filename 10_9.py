try:
    with open('cats.txt') as my_file:
        contents = my_file.read()

except FileNotFoundError:
    pass

else:
    print('-x-x-x-x- Cats -x-x-x-x-')
    print(contents)


try:
    with open('dogs.txt') as my_file:
        contents = my_file.read()

except FileNotFoundError:
    pass

else:
    print('-x-x-x-x- Dogs -x-x-x-x-')
    print(contents)