'''Encapsulation is the key concepts of oops prinicples is used to bundle the data and methods that operates in a single unit.
restricted direct acess to object compenents

Key concpets

 Public Members: Accessible from anywhere.

Protected Members: Prefixed with a single underscore _. Meant to be treated as "protected" (suggests limited access).

Private Members: Prefixed with double underscore __. Name mangled to prevent direct access.
 '''

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner  #Public Member
        self.__balance = balance #Private Member

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Amount ${amount}")
        else:
            print("Amount should be positive")
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f" withdraw ${amount}")
        else:
            print("Insufficient funds")

    def get_balance(self,balance):
        return self.__balance

b = BankAccount("Poorna", 1000)
b.deposit(100)
b.withdraw(50)
print(b.__balance) #Attribute Error beacause trying to access the private member