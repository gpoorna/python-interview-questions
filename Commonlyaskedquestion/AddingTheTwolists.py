lst1 = [10,20,30]
lst2 = [25,35,45]
res_lst = []
for i in range(0, len(lst1)): #3
    #res_lst = lst1.append(lst1[i]+lst2[i]) #incorrect logic
    res_lst.append(lst1[i]+lst2[i])
print(res_lst)
