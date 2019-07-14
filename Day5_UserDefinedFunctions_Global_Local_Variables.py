'''
def func1():
    pass

def func2(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    print(result)

func2(1,5)

def func3(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    return result

f=func3(1,10)
print(f)

def sum(start,end):
    if (start>end):
        print("Start value should be less than end value")
        return
    result = 0
    for i in range(start, end + 1):
        result = result + i
    return result

s=sum(5,1)
print(s)   # If you do not explicitly return any value, then a special value "None" is always returned

s=sum(1,5)
print(s)



def test():
    i=100
    return

print(test()) '''


#Global variables and local variables

global_var=100

def func():
    local_var=200
    print(local_var) #200 becoz it is local inside the function
    print(global_var) #100 becoz it is declared as global variable

func()


xy=100

def cool():
    xy=200
    print(xy)

cool() # 200 becoz it is declared inside the function


t=200

def increment():
    global t
    t=100
    print(t)

increment() # 100, since t is declared as global variable

def foo():
    global x
    x=500
    print(x)

foo()
print(x) # 500 as x is declared as global variable


# passing arguments

#positional arguments

def func(i,j):
    print(i,j)

func(10,20) # 10, 20
func(20,10) #20, 10

def func12(i,j=0):
    print(i,j)

func12(10) # 10,0 as j is stored with default value as 0

def func13(i,j=0):
    print(i,j)

func13(10,20) # 10, 20 as j is passed with some value while calling the function. It will overwrite the default value specified in the function



#keyword arguments

def wish1(name,greeting):
    print(greeting+" "+name)

wish1("Rajesh","Hello") #Hello Rajesh
wish1(greeting="Hello",name="Surya") #Hello Surya


#mixed arguments

def my_func(a,b,c):
    print(a,b,c)

my_func(10,c=20,b=100) # 10,100,20

#my_func(c=20,b=100,10) #Error, positional argument must appear before keyword argument























