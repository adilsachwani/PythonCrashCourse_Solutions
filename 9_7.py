class User():
    def __init__(self, first_name, last_name, age, education):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " - " + str(self.age))
        print(self.education.title())

    def greet_user(self):
        print("Welcome " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, education, privilages):
        super().__init__(first_name,last_name,age,education)
        self.privilages = privilages

    def display_privilages(self):
        for privilage in self.privilages:
            print(self.first_name.title() + " " + privilage + ".")

privilages = ['can add post','can delete post','can ban user']

adil = Admin("adil","sachwani",21,"BCIT - NEDUET",privilages)

adil.display_privilages()