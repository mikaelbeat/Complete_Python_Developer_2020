
def demo_function(value=0):
    try:
        return value + 5
    except TypeError as err:
        return err