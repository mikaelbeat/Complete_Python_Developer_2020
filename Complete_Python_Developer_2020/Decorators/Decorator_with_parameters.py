
def demo_decorator(func):
    def wrapper(*args, **kwargs):
        print("********** Header **********")
        func(*args, **kwargs)
        print("********** Footer **********\n")
    return wrapper


@demo_decorator
def hello(data):
    print(data)
    
def hello_again(data):
    print(data)
    
def hello_for_third_time(data):
    print(data)

    
hello("First")

hello2 = demo_decorator(hello_again)
hello2("Second")

demo_decorator(hello_for_third_time)("Third")
