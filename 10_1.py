filepath = 'learning_python.txt'

with open(filepath) as file_object:
    data = file_object.read()
    print(data)

print()

with open(filepath) as file_object:
    for object in file_object:
        print(object.strip())

print()

with open(filepath) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())