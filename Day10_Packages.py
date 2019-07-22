

#Approach 1

import sys
sys.path.append("C:/Users/RS042424/PycharmProjects/POT1/pack1")
sys.path.append("C:/Users/RS042424/PycharmProjects/POT1/pack2")

import a_withFunction
a_withFunction.display()

import b_withFunction
b_withFunction.show()



#Approach 2

import sys

sys.path.append("C:/Users/RS042424/PycharmProjects/POT1/pack1")
from a_withFunction import *
display()


sys.path.append("C:/Users/RS042424/PycharmProjects/POT1/pack2")
from b_withFunction import *
show()


#Exception Handling

""" 
Multi except blocks...else..finally

try:
	statement;
except Exception1 : #This will execute when Exception1 has occured 
	----
except Exception2 : #This will execute when Exception1 has occured
	----
except Exception3 : #This will execute when Exception1 has occured
	----
else:
	------ //Executed else block when No exceptions found
finally:
	-------//This will execute everytime no matter what


"""


#try...except
try:
    num1,num2=10,0
    result=num1/num2
    print(result)
except ZeroDivisionError as e:
    print("ZeroDivisionError.... Exception occured and handled")
except SyntaxError as s:
    print("SyntaxError ..... Exception occured and Handled")
except:
    print("Invalid Input")
else:
    print("Entered into Else Block, No Exceptions found")
finally:
    print("Entered into Finally Block, program completed")



#ZeroDivisionError
#SyntaxError

