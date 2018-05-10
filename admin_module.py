from user_module import User

class Admin(User):
    def __init__(self, first_name, last_name, age, education, priv):
        super().__init__(first_name,last_name,age,education)
        self.privileges = Privileges(priv)

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def display_privileges(self):
        for privilege in self.privileges:
            print("Admin " + privilege + ".")