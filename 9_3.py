class User():
    def __init__(self, first_name, last_name, age, education):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " - " + str(self.age))
        print(self.education.title())

    def greet_user(self):
        print("Welcome " + self.first_name.title())


adil = User("adil","sachwani",21,"BCIT - NEDUET")
ahsan = User("ahsan","amir ali",20,"CS - SZABIST")

adil.greet_user()
adil.describe_user()

ahsan.greet_user()
ahsan.describe_user()