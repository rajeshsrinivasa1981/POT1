
# Creating an class and object
class MyClass1:
    def func(self):
        pass

    def display(self,name):
        print("Name is:",name)

obj1=MyClass1()
obj1.func()
obj1.display("Rajesh")

#Instance method and Static method

class MyClass2:
    def m1(self):  # Access these methods only through objects
        print("This is instance method")

    @staticmethod
    def m2(): # Access these methods directly using class
        print("This is static method")

obj2=MyClass2()
obj2.m1() #calling instance method through object creation

MyClass2.m2() #calling static method through class

#Declaring variables inside the class

class MyClass3:
    a,b=10,20
    def add(self):
        print(self.a+self.b)

cal=MyClass3()
cal.add()

#Declaring Local, Class and Global Variables -

#Declaring Local, Class and Global variables with different variable names

i,j=50,40
class MyClass4:
    a,b=10,20 #Class Variables

    def sum(self,x,y):
        print(x+y) #local variables
        print(self.a+self.b) #accessing class variables
        print(i+j)

cal=MyClass4()
cal.sum(100,200)

#Declaring Local, Class and Global variables with same variable names

i,j=50,40
class MyClass4:
    i,j=10,20 #Class Variables

    def sum(self,i,j):
        print(i+j) #local variables
        print(self.i+self.j) #accessing class variables
        print(globals()['i']+globals()['j'])

cal=MyClass4()
cal.sum(100,200)


#One class with multiple objects

class MyClass5:
    def display(self,name):
        print("Name is:",name)

obj1=MyClass5()
obj1.display("Rajesh")


#named and namesless object:

class MyClass6:

    def display(self):
        print("This is diplay method")

obj1=MyClass6()
obj1.display() # Named object creation

MyClass6().display() #Nameless object creation


#Constructor

class MyClass7:
    def m1(self):
        print("Good morning")

    def __init__(self):  # This is always executed at the begining of the class
        print("This is constructor")

obj=MyClass7()
obj.m1()

######### Example11:converting local variables in to class variables (Here Method taking arguments)
class MyClass8:
    def values(self,val1,val2):
        print(val1,val2)
        self.val1=val1
        self.val2=val2

    def add(self):
        print(self.val1+self.val2)

mc=MyClass8()
mc.values(10,20)
mc.add()

######### Example11:converting local variables in to class variables (Here constructor taking arguments)

class MyClass:
    def __init__(self,val1,val2):
        print(val1, val2)
        self.val1 = val1
        self.val2 = val2

    def add(self):
        print(self.val1 + self.val2)

mc=MyClass(40,50)
mc.add()

class MyClass:
    def __str__(self):
        return " I am Rajesh"

c=MyClass()
print(c)


class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        return("emp id:{}   emp name:{}   emp sal:{}".format(self.eid,self.ename,self.esal))


mc=Emp(101,"Rajesh","100000")
print(mc)


class Myclass:
    def __del__(self):
        print("Objects destroyed")

m1=Myclass()
m2=Myclass()

del m1
del m2























