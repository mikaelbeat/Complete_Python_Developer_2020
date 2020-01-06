
data = [1, "Cat", 5, "IPhone"]

# Adding methods

# Len method starts counting from 1 instead of 0
print("len method, returns length of the list")
print(len(data))
print("\n")

# Add value to list using append
print("Append method, computer value added")
data.append("Computer")
print(data)
print("\n")

# Add value to list in given index
print("Add method, banana value added to index 2")
data.insert(2, "Banana")
print(data)
print("\n")

# Extend method extends the list by adding values to end of the list
print("Extend method, Apple and PS5 values added to list")
data.extend(["Apple", "PS5"])
print(data)
print("\n")

# Removing methods

# Pop method removes last value from the list
print("Pop method, last value PS5 removed")
data.pop()
print(data)
print("\n")

# Pop method with index removes value from given index
print("Pop method with index, cat value removed")
data.pop(1)
print(data)
print("\n")

# Remove method removes given value from the list
print("Remove method removes given value from the list, computer removed")
data.remove("Computer")
print(data)
print("\n")

# Clear method removes all values from the list
print("Clear metohd removes all valus from the list")
data.clear()
print(data)


# Lecture 42