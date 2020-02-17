
with open("data_file2.txt", mode="r+") as data:
    data.write("First entry! ")

with open("data_file2.txt", mode="r") as data:
    print(data.read())

with open("data_file2.txt", mode="a") as data:
    data.write("Second entry!")

with open("data_file2.txt", mode="r") as data:
    print(data.read())