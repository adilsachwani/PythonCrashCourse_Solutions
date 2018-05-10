class Restraunt():
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restraunt_name.title() + " cooks " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print("Restraunt is open")

r1 = Restraunt("Chop Soy","Chinese")

print(r1.restraunt_name)
print(r1.cuisine_type)

r1.describe_restaurant()
r1.open_restaurant()