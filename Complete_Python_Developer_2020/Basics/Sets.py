
# Set is unordered list with unique values

data = {1, 2, 3, 4, 5, 5}
data2 = {4, 5, 6, 7}

print(data)

print("\n")

print(f"Set difference {data.difference(data2)}\n")

print(f"Discarded value 5 from data.")
data.discard(5)
print(data)

print("\n")

# data.difference_update(data2) - Leaves to data set only values which are unique in it
# data.intersection(data2) - Prints values which are found both sets -> 4, 5 in this case
# data.isdisjoint(data2) - Returs false is sets have same values
# data.issubset(data2) - Checks if given set have all values are found in another set
# data.issuperset(data2) - Cheks if given set have all values in another set
# data.union(data2) - Unites sets and removes duplicates