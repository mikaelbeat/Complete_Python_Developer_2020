

print("\n********** Using Set comprehension **********\n")

data = {char for char in "Hello again!"}

print(data)


print("\n********** Using Set comprehension example 2 **********\n")

data = {num for num in range(0 , 21)}

print(data)


print("\n********** Using Set comprehension example 3 **********\n")

data = {num * 2 for num in range(0, 21)}

print(data)


print("\n********** Using Set comprehension example 4 **********\n")

data = {num * 2 for num in range(0, 21) if num % 2 ==0}

print(data)
