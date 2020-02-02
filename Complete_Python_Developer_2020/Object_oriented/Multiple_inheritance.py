
class User():
    def __init__(self):
        pass
    
    def sign_(self):
        print(f"Character {self.name} logged in\n")
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def cast_fireball(self):
        print(f"Character {self.name} casted fireball!\n")
        
class Archer(User):
    def __init__(self, name, dexterity):
        self.name = name
        self.dexterity = dexterity
        
    def barrage_of_arrows(self):
        print(f"Character {self.name} shot barrage of arrows!\n")
        
class Mage_archer(Wizard, Archer):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
        
wizard1 = Wizard("Merlin", 100)
wizard1.sign_()

archer1 = Archer("William Tell", 100)
archer1.sign_()

mage_archer1 = Mage_archer("Legolas", 100)
mage_archer1.sign_()
mage_archer1.cast_fireball()
mage_archer1.barrage_of_arrows()