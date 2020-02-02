
# Reduce is a really useful function for performing some computation on a list and returning the result. 
# It applies a rolling computation to sequential pairs of values in a list. 
# For example, if you wanted to compute the product of a list of integers.

from functools import reduce

data1 = [1, 2, 3, 4, 5]
data2 = ["One", "Two", "Three", "Four", "Five"]

def demo(acc, item):
    print(acc, item)
    return acc + item

print(reduce(demo, data1, 0))