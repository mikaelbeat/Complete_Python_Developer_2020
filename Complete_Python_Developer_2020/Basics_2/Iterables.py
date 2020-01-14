
monster = {
    "Name": "Snake",
    "Hitpoints": 150,
    "Armour": 50
    }


print("\n********** All data **********\n")

for key, value in monster.items():
    print(key, value)
    
    
print("\n********** Values **********\n")
    
for value in monster.values():
    print(value)
    
    
print("\n********** Keys **********\n")
    
for key in monster.keys():
    print(key)