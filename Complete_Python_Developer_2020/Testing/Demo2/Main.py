
def demo_function(value1, value2):
    try:
        return value1 + value2
    except TypeError as err:
        return err