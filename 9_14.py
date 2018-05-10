from random import randint

class Dice():
    def __init__(self):
        self.sides = 6

    def roll_dice(self):
        x = randint(1,self.sides)
        print("Random Numbers: " + str(x) + "\tSides: " + str(self.sides))

x=1
six = Dice()
ten = Dice()
twenty = Dice()

ten.sides = 10
twenty.sides = 20

while x<=30:
    if x<=10:
        six.roll_dice()
    elif x<=20:
        ten.roll_dice()
    else:
        twenty.roll_dice()

    x += 1