**(2) Variable & Simple Data Types**  

01- print(str.title()) #case the string  
02- print(str.upper()) #uppercase the string  
03- print(str.lower()) #lowercase the string  
04- print("\tPython") #whitespaces using tabs  
05- favorite_language = favorite_language.rstrip() #remove whitespaces from right side  
06- message = "Happy " + str(age) + "rd Birthday!" #print string with integer  

**(3) Introducing Lists**  

01- bicycles = ['trek', 'cannondale', 'redline', 'specialized']  
02- print(bicycles[0])  
03- print(bicycles[-1])  
04- motorcycles[0] = 'ducati'  
05- motorcycles.append('ducati')  
06- motorcycles.insert(0, 'ducati')  
07- del motorcycles[0]  
08- popped_motorcycle = motorcycles.pop()   
09- first_owned = motorcycles.pop(0)  
10- cars.sort()  
11- cars.sort(reverse=True)  
12- print(sorted(cars))  
13- cars.reverse()  
14- print(len(cars))  

**(4) Working with Lists**  

01- for m in magicians:  
        print(m)  
02- for value in range(1,5):  
        print(value)  
03- numbers = list(range(1,6))  

04- min(digits)
05- max(digits)
06- sum(digits)
07- squares = [value**2 for value in range(1,11)] #list comprehensions
08- print(players[0:3])
09- print(players[:3])
10- print(players[0:])
11- print(players[-3:])
12- friend_foods = my_foods[:]
13- dimensions = (200, 50) #tuple - cant be changed
Python Enhancement Proposal (PEP)
14- Indentation: Use four spaces per indentation
15- Line length: each line should be less than 80 characters
16- Blank lines

**(5) IF Statements**  

01- if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
02- 'mushrooms' in requested_toppings
03- if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")
04- if age < 4:
        price = 0
    elif age < 18:
        price = 5
    else:
        price = 10
05- if requested_toppings: #checking list empty or not

**(6) Dictionaries**  

01- alien_0 = {'color': 'green', 'points': 5}
02- alien_0['color'] = 'yellow'
03- del alien_0['points'
04- for key, value in user_0.items():
        print("\nKey: " + key)
        print("Value: " + value)
05- for language in favorite_languages.values():
        print(language.title())
06- pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
        }

**(7) User Input and While Loops**  

01- message = input("Tell me something, and I will repeat it back to you: ")
02- prompt = "If you tell us who you are, we can personalize the messages you see." 
    prompt += "\nWhat is your first name? "
03- while current_number <= 5:
        print(current_number)
        current_number += 1
04- while unconfirmed_users:
        current_user = unconfirmed_users.pop()
05- while 'cat' in pets:
        pets.remove('cat')
06- responses[name] = response #dictionary

**(8) Functions**  

01- def function_name(parameter_0, parameter_1='default value'): 
02- describe_pet('hamster','harry'): #positional arguments
03- describe_pet(animal_type='hamster', pet_name='harry') #keyword arguments
04- function_name(list_name[:]) #passing copy of list rather than the actual list
05- def make_pizza(*toppings): #for passing an arbitary number of arguments
06- def build_profile(first, last, **user_info): #double asterik for dictionary
07- import pizza #importing a different module
08- pizza.make_pizza(16, 'pepperoni') #using functions from a module
09- from module_name import function_name #importing specific functions from a module
10- make_pizza(16, 'pepperoni') #using a imported functions from a smodule
11- import pizza as p #alias module
12- from pizza import make_pizza as mp #alias module functions
13- from pizza import * #importing all functions of module

**(9) Classes**  

01- class Dog():
02- def __init__(self, name, age):
        self.name = name
03- my_dog = Dog('willie', 6) #create instance
04- class ElectricCar(Car):
05- def __init__(self, make, model, year):
        super().__init__(make, model, year)

**(10) Files and Exception**  

01- with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents)
02- with open(filename) as file_object:
        for line in file_object:
            print(line)
03- with open(filename) as file_object:
        lines = file_object.readlines()
04- for line in lines:
        pi_string += line.strip()
05- line.replace('Python','C')
06- with open(filename, 'w') as file_object:
        file_object.write("I love programming.")
07- with open(filename, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")
08- try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

09- except FileNotFoundError:
        pass
10- filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
11- with open(filename) as f_obj:
        numbers = json.load(f_obj)                                                               
