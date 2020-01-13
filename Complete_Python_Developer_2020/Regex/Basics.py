
import re


data = "Search this inside of this text please!"
pattern = re.compile(r"([a-zA-Z]).([a])")

result = pattern.search(data)

print(result)
