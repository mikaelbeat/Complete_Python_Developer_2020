
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"It took {end_time - start_time}s to run slow function.")
        return result
    return wrapper


@performance
def slow_function():
    for i in range(10000000):
        i*5
        
        
slow_function()