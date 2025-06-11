numList = [10,35,85,15,100]
maxNum = numList[0] #10
for num in numList: #num =1=-
    if maxNum < num: #check for the condition 10<10 false ,comes out of loop, 10<35, 10<85 ,10<15 ,10<100
        maxNum = num #35,85,15 ,100
print(maxNum)