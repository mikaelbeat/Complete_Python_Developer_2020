
class User():
    def sign_(self):
        print("Logged in")
        
class Wizard(User):
    pass

class Archer(User):
    pass


wizard1 = Wizard()
wizard1.sign_()