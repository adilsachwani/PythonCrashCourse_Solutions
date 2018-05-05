def make_car(manufacturer, model, **information): #function taking three arguments including a dictionary
    car_profile={}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model

    for key,value in information.items():
        car_profile[key] = value

    return car_profile

car = make_car("Toyota", 1996, color="red", speed=1200) #passing 4 arguments where last two are additonal iones as per choice

print(car) #printing car dictionary
