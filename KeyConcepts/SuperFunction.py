#super() function is used to refer the parent class or super class. it enables you to call the parent methods from the subclasses
#enables you to cutomise the functionality from parent class

class EMP:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


    def employee(self):
        print("works from office")

class FreeLance(EMP):
    def __init__(self,name, id, age, Email):
        super().__init__(name, id, age) #calling the parent class constructor and overiding it or making it customised
        self.Email = Email



F = FreeLance("Ravi", 10, 25, "ravi@cgi.com")
F.employee()
print(F.name, "", F.id, "", F.age, "", F.Email)

