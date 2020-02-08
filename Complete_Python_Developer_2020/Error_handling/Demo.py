
data = [1, 2, 3]

try:
    print(data[3])
except IndexError as err:
    print(f"Index error! --> {err}")
finally:
    print("Hello from finally block!")