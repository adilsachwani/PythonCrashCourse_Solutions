personOne = {'name':'adil',
             'age' : '22',
             'city' : 'karachi'}

personTwo = {'name':'sabe',
             'age' : '21',
             'city' : 'lahore'}

people = [personOne,personTwo]

for person in people:
    print(person['name'].title() + "'s age is " + person['age'] + " and he lives in " + person['city'].title())