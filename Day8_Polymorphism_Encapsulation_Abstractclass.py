#Polymorphism

#overriding

class Parent:
    name="Rajesh"

class Child(Parent):
    name="David"

obj=Child()
print(obj.name)

class Bank:
    def RateOfInterest(self):
        return 0

class ICICIBank(Bank):
    def RateOfInterest(self):
        return 9.5

class AXISBank(Bank):
    def RateOfInterest(self):
        return 10.5

obj=ICICIBank()
print(obj.RateOfInterest())

obj=AXISBank()
print(obj.RateOfInterest())


## Overloading

class Human:
    def SayHello(self,name=None):
        if name is not None:
            print("Hello"+name)
        else:
            print("Hello")

obj=Human()
obj.SayHello()
obj.SayHello("Rajesh")


#Encapsulation - Declaring private variables and private methods

#Private variables can accessed only within a method ; NOT OUTSIDE THE METHOD
class Parent:
    __a=10 # If we __variablename = value then it is declared as private variable
    def disp(self):
        print(self.__a)

obj=Parent()
obj.disp()
#print(obj.__a) #AttributeError: 'Parent' object has no attribute '__a'

#Private methods can accessed only within a method ; NOT OUTSIDE THE METHOD

class Myclass:
    def __disp(self):
        print("This is private method")

    def disp2(self):
        print("This is display2 method")
        self.__disp() #calling private method


obj=Myclass()
obj.disp2()

"""
Abstract
----------------------
1) Abstract class contains only abstract methods.
2) Abstract method - method contains only definition but not body.
3) Abstract methods can be implemented using sub class
4) We cannot create object of abstract class
"""

from abc import ABC,abstractmethod
class A(ABC):

    @abstractmethod
    def display(self):
        pass

class B(A):
    def display(self):
        print("Welcome")

obj=B()
obj.display()


#############

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def VehicleType(self):
        pass

class Maruti(Vehicle):
    def VehicleType(self):
        print("S-Cross")

class Hyundai(Vehicle):
    def VehicleType(self):
        print("Creta")

class Ford(Vehicle):
    def VehicleType(self):
        print("Ecosport")


obj=Ford()
obj.VehicleType()

obj=Hyundai()
obj.VehicleType()

obj=Maruti()
obj.VehicleType()


##########
from abc import ABC,abstractmethod
class Building(ABC):

    @abstractmethod
    def CommercialBuilding(self):
        pass

    @abstractmethod
    def PrivateBuilding(self):
        pass

class Office:
    def CommercialBuilding(self):
        print("This office space is for Infosys")

class Home:
    def PrivateBuilding(self):
        print("This building space is for Home Construction")

obj=Office()
obj.CommercialBuilding()

obj=Home()
obj.PrivateBuilding()











