
# In simple words, the filter() method filters the given iterable with the help of a function,
#  that tests each element in the iterable to be true or not.


data = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

def only_odd(item):
	return item % 2 !=0

print(list(filter(only_odd, data)))