

def args_demo(*args):
    print(args)
    print(sum(args))
    
print("\n********** Args **********\n")
args_demo(1, 2, 3, 4, 5)


def kwargs_demo(**kwargs):
    print(kwargs)
    total = 0
    for value in kwargs.values():
        total += value
    print(total)
    
print("\n********** Kwargs **********\n")
kwargs_demo(value1= 5, value2=5)
