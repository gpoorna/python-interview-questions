 #Define Class: class is a blue print for creating the objects
#objects is an instance of a class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def works(self):
        print(f"Employeer: {self.name} - {self.age}")

e = Employee("RamaKrishna", "25")
e.works()