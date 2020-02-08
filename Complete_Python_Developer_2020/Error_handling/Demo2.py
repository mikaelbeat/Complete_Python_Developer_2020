

while True:
    try:
        print("\nCALCULATOR\n")
        value1 = int(input("Give first value: "))
        value2 = int(input("Give second value: "))
        result = value2 / value1
        print(f"Result for reducing {value1} from {value2} is {result}")
    except ValueError:
        print("Please input only integer values!\n")
        continue
    except ZeroDivisionError:
        print("First value is bigger than second value!\n")
        break

