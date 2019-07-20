#Single Inheritance

'''
class A1:
    x,y=100,200
    def m1(self):
        print(self.x+self.y)

class B1(A1):
    a,b=300,400
    def m2(self):
        print(self.a+self.b)

bobj = B1()
bobj.m1()
bobj.m2()

#Multilevel Inheritance

class A2:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B2(A2):
    a, b = 300, 400
    def m2(self):
        print(self.a + self.b)

class C2(B2):
    i, j = 50, 40
    def m3(self):
        print(self.i + self.j)


cobj=C2()
cobj.m3()
cobj.m2()
cobj.m1()
'''
#Heirarchy Inheritance
'''
class A:
    x,y=15,15
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A):
    i,j=50,100
    def m3(self):
        print(self.i+self.j)

bobj = B()
bobj.m1()
bobj.m2()

cobj=C()
cobj.m1()
cobj.m3()
'''

# Multiple Inheritance
'''
class A:
    x,y=15,15
    def m1(self):
        print(self.x+self.y)

class B():
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A,B):
    i,j=50,100
    def m3(self):
        print(self.i+self.j)


cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()
'''


#calling parent class method using super class

"""
class A:
    def m1(self):
        print("This is m1 method from Class A")

class B(A):
    def m2(self):
        print("This is m2 methos from Class B")
        super().m1()

bobj=B()
bobj.m2()
"""

#calling parent class variables (with different variable names)

'''
class A:
    a,b=10,20

class B(A):
    i,j=100,200
    def m2(self,x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)

bobj=B()
bobj.m2(1000,2000)
'''

#calling parent class variables with super class (with different variable names)

""" 
a,b=900,1000
class A:
    a,b=10,20

class B(A):
    a,b=100,200
    def m2(self,a,b):
        print(a+b) #local variables
        print(self.a+self.b) #class variables
        print(super().a+super().b) #super class variables
        print(globals()['a']+globals()['b']) #global variables

bobj=B()
bobj.m2(10,10)
"""

#calling parent class constructor when child class has No constructor

""" 
class A:
   def __init__(self):
       print("Constructor of A")

class B(A):
    def __init__(self):
        print("Constructor of B")
        super().__init__()

bobj=B()
"""

# More examples

class Parent:
    def __init__(self,first,last):
        self.first=first
        self.last=last

class Child(Parent):
    def __init__(self,first,last,id):
        super().__init__(first,last)
        self.id=id

    def __str__(self):
        return ("Emp:{} Firstname:{}    Lastname:{}       ".format(self.id,self.first,self.last))

obj=Child(101,"Rajesh","Srinivasa")
print(obj)