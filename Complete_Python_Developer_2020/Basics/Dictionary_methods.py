

user = {
    "Name": "Snake",
    "Occupation": "Agent"
    }


print("name" in user.keys())
print("agent" in user.values())
print(user.items())
#print(user.clear())

print("\n")

user2 = user.copy()
print(user2)

print("\n")

print(user2.pop("Occupation"))
print(user2)

print("\n")

print(user2.update({"Name": "Solid Snake"}))
print(user2)