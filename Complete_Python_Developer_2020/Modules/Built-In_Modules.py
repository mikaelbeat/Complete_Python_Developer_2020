
import random

data = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]

print("Randon value between 1 and 10")
print(random.randint(1, 10))
print("\n")

print("Randon value from given list")
print(random.choice(["Cat", 12345, "Snake", {"Heloy"}]))
print("\n")

print("Randomize whole list")
random.shuffle(data)
print(data)
print("\n")