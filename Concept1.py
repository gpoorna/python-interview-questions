#Differnce b/w list and tuple
#list are denoted with square brackets and lists are mutable in nature
#we can store both homogenous and hetrogenous data in list and tuple

list_numbers = [1,2,3,4]
list_numbers[1] = 34
print(list_numbers)
list_numbers.pop(2)
print(list_numbers)

tuple_strings = (10,20,30,40)
#tuple_strings[1] = 35 #tuples does not support value assignment and tuples are imutable in nature
print(tuple_strings)
#tuples should be used when there is when we do need to modify the records or elemrnts