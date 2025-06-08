''' Absatrction is a process of hiding implemenstsion details and show only necessary details to the users,
 we can acheive the abstarction using abstarct classes and abstarction can be created using the abc (abstarct base class module)

Notes: Abstarct class is a class in which one or more abstract methods are defined.when method is declared
inside the class without it's implementaion is known as abstract method.

Abstract Method: In Python, abstract method feature is not a default feature. To create abstract method and abstract classes we have to import the "ABC" and "abstractmethod" classes from abc (Abstract Base Class) library
 '''
from abc import ABC, abstractmethod


class BaseClass(ABC):
    @abstractmethod
    def method1(self):
        pass
