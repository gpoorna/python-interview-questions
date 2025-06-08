# lambda function in a python is small and anonymous function that can have multiple arguments but
# only one expression
# common usage of lamda function includes map functiom
# map function is used to modify the logic inside the list.
#syntax of lamda function lambda argument:expression

def add(x, y):
    return x + y

data = lambda x, y: x + y
print(add(5,20))
