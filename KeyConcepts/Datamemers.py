#usage of local varaibles, instance varaibles and static variables

class Student:
    age = 25 #static varaibles
    college_name = "BIT" #static varaibles

    def __init__(self,name, year_of_pass_out):
        self.name = name #instance variables
        self.year_of_pass_out = year_of_pass_out  #instance variables

    def getCGPA(self, percentage):
        print("The percentage of student", percentage)


s = Student("Raja", "2021") 
s.getCGPA(80)
print(Student.age) #Accessing the static variables using class name
print(Student.college_name)
print(s.name)

