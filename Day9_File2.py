
'''
#Approach 1
import Day9_File1

Day9_File1.add(3,4)
Day9_File1.mul(10,4)

#Approach 2

from Day9_File1 import add,mul

add(10,5)
mul(30,5)

#Approach 3 -

from Day9_File1 import *

add(5,10)
mul(6,5)


# Same functions in 2 modules

#Approach 1

import Day9_File1
import Day9_File3

Day9_File1.add(3,8)
Day9_File1.mul(4,8)

Day9_File3.add(3,7)
Day9_File3.mul(4,8)

# Approach 2
from Day9_File1 import *
add(10,2)
mul(10,4)

from Day9_File3 import *

add(5,6)
mul(4,5)

'''

#imporinting classes with methods

#Appraoch 1

import Day9_File1
import Day9_File3


obj=Day9_File1.Animal()
obj.display()

obj2=Day9_File3.Bird()
obj2.display()

#Apprach 2

from Day9_File1 import Animal
from Day9_File3 import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()





