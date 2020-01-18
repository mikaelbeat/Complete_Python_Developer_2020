
print("\n********** Range with variable **********\n")

for value in range(0, 5):
    print(value)
    
    
print("\n********** Range without variable **********\n")

for _ in range(0, 5):
    print(_)
    
    
print("\n********** Range backwards **********\n")

for _ in range(4, 0, -1):
    print(_)
    
    
print("\n********** Range looping **********\n")

for _ in range(2):
    print(list(range(5)))