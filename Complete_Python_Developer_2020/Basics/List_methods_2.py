
data = ["IPhone", 1, "Cat", 5, "IPhone"]
data2 = [3, 2, 6, 5, 4, 9, 7]

# Index method return the location of given value
print("Index method return the location of given value")
print(data.index("Cat"))
print("\n")

# Index method searching value in given range
print("Index method searching value in given range")
print(data.index("Cat", 0, 3))
print("\n")

# In method returns boolean value if given value is in the list
print("In method returns boolean value if given value is in the list")
print("IPhone" in data)
print("\n")

# Count method return how many times given value is in the list
print("Count method return how many times given value is in the list")
print(data.count("IPhone"))
print("\n")

# Sort method sorts the list
print("Sort method sorts the list")
data2.sort()
print(data2)
print("\n")

# Reverse method sorts the list in reverse order
print("Reverse method sorts the list in reverse order")
data2.reverse()
print(data2)
print("\n")