
from collections import Counter, defaultdict, OrderedDict

print("********** Counter module **********\n")

# Count how many times item is in the list
data1 = [1, 2, 3, 4, 5, 5]
print(Counter(data1))

data2 = "Hello there!"
print(Counter(data2))


print("\n********** defaultdict module **********\n")

# Returns default value is called item is not in the dictionary

data3 = defaultdict(lambda: "Value not in dictionary!", {"a" : 1, 
         "b" : 2})

print(data3["c"])