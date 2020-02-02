
class User():
    def __init__(self, email):
        self.email = email
    
    def sign_(self):
        print(f"Wizard {self.name} logged in")
        

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power


wizard1 = Wizard("Merlin", 100, "merlin@gmail.com")
wizard1.sign_()