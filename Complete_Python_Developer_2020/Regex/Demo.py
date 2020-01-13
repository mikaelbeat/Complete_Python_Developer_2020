
import re


data = "Search this inside of this text please!"

result = re.search("this", data)

print(result)


print("\n********** Another approach **********\n")

pattern = re.compile("this")

result = pattern.search(data)
result2 = pattern.findall(data)
result3 = pattern.fullmatch(data)

print(result)
print(result2)
print(result3)



