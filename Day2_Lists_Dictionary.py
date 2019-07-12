list1=[10,20,30,40]

ex1=[x for x in range(10)]
print(ex1)

ex2=[x+1 for x in range(10)]
print(ex2)


list=["a","ab","bc","cd","a"]
for i in list:
    print(i, end= " ")
print()

list1.append(80) # it appends the data to existing list.
print(list1)

print(list1.count(30))

list2=[90,80,100,120]

list3=list1+list2
print(list3)

list4= list1*5
print(list4)


list1.extend(list2) # here elements of list2 are added to list1
print(list1)

list1.pop(3) #removes the value based on the index
print(list1)

list1.remove(120) #removed the value based on the object
print(list1)

list1.insert(3,900) #inserts the value at the specifiex index
print(list1)


list1.reverse() #reverse the list of values
print(list1)


list5=list1.copy() #it copies the list into another list.
print(list5)

list1.sort() #it sorts the list in ascending order
print(list1)

list1.sort(reverse=True) # It sorts the list in descending order
print(list1)

print(20 in list1) #True

print(20 not in list1) #False

print(len(list1))  #The number of elements in the list

print(max(list1)) #prints the maxmimum number in the list

print(min(list1)) #prints the minimum number in the list


#Slicing

print(list1)

s3= list1[2:9]
print(s3)

s3=list1[2:-1]
print(s3)

#Dictionary
Descripton={'Color':'Green','Points':'5','Name':'Ramesh'}
print(Descripton)

Descripton['Height']='5.5' #Adding Key and Value in the dictionary
print(Descripton)

print("The color is"+" "+Descripton['Color'])#Retreiving the value in the dictionary

print(Descripton.keys()) #prints the keys in the dictionary

print(Descripton.values()) #prints the values in the dictionary

del Descripton['Height'] #Deletes the Key and Value
print((Descripton))

for x in Descripton:
    print(x,":",Descripton[x])

print(len(Descripton))

d1 = {"mike":41, "bob":3}
d2 = {"bob":3, "mike":42}

print(d1==d2) #True/False

print(Descripton)

Descripton['Car Make']='Hyundai'
print(Descripton)

Descripton.popitem() #Randomly selects the item in the dictionary and removed the selected item
print(Descripton)

print(Descripton.get('Color'))

print(Descripton.pop('Points'))
print(Descripton)









