import re

specialcharacters = "!@#$%^&*()"
count = re.sub('[\w]+', '', specialcharacters)
print(len(count))