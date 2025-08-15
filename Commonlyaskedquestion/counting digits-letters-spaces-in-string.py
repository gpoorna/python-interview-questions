import re

name = "python is 1"
digitcount = re.sub("[^0-9]","", name)
lettercount = re.sub("^a-zA-Z", "", name)
spacecount = re.findall("[ \n]", name)

print(digitcount)
print(lettercount)
print(spacecount)