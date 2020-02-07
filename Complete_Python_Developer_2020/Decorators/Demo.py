
def demo_decorator(func):
    def wrapper():
        print("********** Header **********")
        func()
        print("********** Footer **********\n")
    return wrapper


@demo_decorator
def hello():
    print("HELLO!!!")
    
def hello_again():
    print("HELLO AGAIN!!!")
    
def hello_for_third_time():
    print("HELLO FOR THIRD TIME!!!")

    
hello()

hello2 = demo_decorator(hello_again)
hello2()

demo_decorator(hello_for_third_time)()
