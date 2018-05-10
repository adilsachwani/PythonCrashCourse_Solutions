class Restraunt():
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restraunt_name.title() + " cooks " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print("Restraunt is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def  increment_number_served(self, number):
        self.number_served += number

restraunt = Restraunt("Chop Soy","Chinese")

print(restraunt.number_served)
restraunt.number_served = 54
print(restraunt.number_served)
restraunt.set_number_served(23)
print(restraunt.number_served)
restraunt.increment_number_served(7)
print(restraunt.number_served)