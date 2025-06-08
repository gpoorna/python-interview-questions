from abc import ABC, abstractmethod


class CAR(ABC):
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    #we can define the method, but method won't be having any body
    @abstractmethod
    def PrintPassDetails(self):
        pass

    #create a concreate method: can have the body
    def accelrate(self):
        print("acclearator pressed")

    def break_applied(self):
        print("break has been applied")


class Toyota(CAR):
    def PrintPassDetails(self):
        print("Model", self.model)
        print("Brand", self.brand)
        print("year", self.year)

    def sunroof(self):
        print("we don't have sunroof feature")

class Benz(CAR):
    def PrintPassDetails(self):
        print("Model:", self.model)
        print("Brand:", self.brand)
        print("Year:", self.year)

    def sunroof(self):
        print(" sunroof Aviliable ")

c1 = Benz("test","suv", "2010")
c2 = Toyota("tyta", "vas", "2011")
c1.PrintPassDetails()
c1.sunroof()
c2.PrintPassDetails()
c2.sunroof()
