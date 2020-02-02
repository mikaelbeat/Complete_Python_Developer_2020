
# Python map() function is used to apply a function on all the elements of specified iterable and return map object. 
# Python map object is an iterator, so we can iterate over its elements.


def multiply(data):
    return data * 2

print(list(map(multiply, [1, 2, 3])))