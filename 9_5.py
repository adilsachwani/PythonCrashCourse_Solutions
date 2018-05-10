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

adil = User("adil","sachwani",21,"BCIT - NEDUET")
ahsan = User("ahsan","amir ali",20,"CS - SZABIST")

adil.increment_login_attempts()
adil.increment_login_attempts()
adil.increment_login_attempts()

print(adil.login_attempts)

adil.reset_login_attempts()

print(adil.login_attempts)