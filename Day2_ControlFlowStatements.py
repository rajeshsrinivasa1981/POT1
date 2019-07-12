#if...else

if True:
    print("Statement1")
else:
    print("statement2")

print("statement1") if True else print("statement2")

a = 10
if a==2:
    print("The number is 2")
elif a==4:
    print("The number is 4")
elif a==6:
    print("The number is 6")
elif a==8:
    print("The number is 8")
elif a==10:
    print("The number is 10")

#While Loop
a=10;               # 10,9,8,7,6,5,4,3,2,1
while a>=1:
    print(a)
    a=a-1

#for loop

for i in range(10): #0,1,2,3,4,5,6,7,8,9
    print(i)

for i in range(1,10,2): #1,3,5,7,9
    print(i)

for i in range(10,1,-1): #10,9,9,8,7,6,5,4,3,2
    print(i)

# Jumping statement break, continue

for i in range(1,10,1): #1,2,3,4
    if i ==5:
        break
    print(i)

for i in range(1,10,1): #1,2,3,4,6,7,8,9
    if i ==5:
        continue
    print(i)

#Working with numbers

x=10
y="welcome"
z=True
w=10.5

print(type(x))
print(type(y))
print(type(z))
print(type(w))

print(type(float(x)))
print(type(int(z)))

print(max(20,30,80))
print(min(20,19,17))

#operators with strings

a="welcome to python"

print(a+"course of learning")

print(a*4)

#Slicing:

str="welcome"

print(str[1:5]) #elco
print(str[1:]) #elcome
print(str[2:-2]) #lco when - is given it will eliminate those many characters of the number specified

print(len(str)) #7
print(max(str)) #w maximium ASCII character in the string
print(min(str)) #c minimum ASCII character in the string

s="welcome to python"

print(s.endswith("thon"))
print(s.startswith("wel"))
print(s.find("come"))
print(s.count("o"))


s = "String in PYTHON"
print(s.capitalize()) #String in python
print(s.title()) #String In Python
print(s.upper()) #STRING IN PYTHON
print(s.lower()) #string in python
print(s.swapcase()) #sTRING  IN python
print(s.replace("in","on")) # Strong on PYTHON
