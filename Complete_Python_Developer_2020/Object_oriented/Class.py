
class PlayerCharacter:
    
    membership = True
    
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points
        
    def heal_yourself(self):
        print(f"Character {self.name} is fully healed!")
        
    @classmethod
    def create_potion(cls, item):
        return f"Created potion from {item}."
    
    @staticmethod
    def create_armour(item):
        return f"Created armour from {item}."
  
        
player1 = PlayerCharacter("Barbarian", 100)
player1.heal_yourself()
print(player1.membership)
print(player1.create_potion("lizard tail"))
print(player1.create_armour("leather"))