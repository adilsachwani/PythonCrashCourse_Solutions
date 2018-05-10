class Restraunt():
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restraunt_name.title() + " cooks " + self.cuisine_type.title() + " food.")

    def open_restaurant(self):
        print("Restraunt is open")

r1 = Restraunt("Chop Soy","Chinese")
r2 = Restraunt("Nosh","Desi")
r3 = Restraunt("Sizzlers","Grill")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()