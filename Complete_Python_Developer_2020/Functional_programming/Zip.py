
# Zip() function is defined as zip(*iterables) . The function takes in iterables as arguments and returns an iterator. 
# This iterator generates a series of tuples containing elements from each iterable.


data1 = [1, 2, 3, 4, 5]
data2 = ["One", "Two", "Three", "Four", "Five"]

print(list(zip(data1, data2)))