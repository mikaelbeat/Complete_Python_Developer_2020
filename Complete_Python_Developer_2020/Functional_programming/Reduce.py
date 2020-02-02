
from functools import reduce

data1 = [1, 2, 3, 4, 5]
data2 = ["One", "Two", "Three", "Four", "Five"]

def demo(acc, item):
    print(acc, item)
    return acc + item

print(reduce(demo, data1, 0))