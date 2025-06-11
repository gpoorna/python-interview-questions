numList = [19,34,3,25,10]
minNum = numList[0]
for num in numList:
    if minNum > num:
        minNum = num
print(minNum)