#Creating Tuples
t=()
print(type(t))
#One number declaration in tuple
t=(10)#This is not tuple, This is int data type
print(type(t))

t1=(10,)# This is tuple data type
print(type(t1))

#tuple is a Heterogeneous data type
t2=(1,2,3,4,5,[1,2,3,'Atul','Ankush'])
print(t2)
t4=(1,2,3,4,(1,2,3,4))
print(t4)

# using type conversion
t3=tuple("hello")
print(t3)

#Accessing Items in tuple 
  #Indexing
  #Slicing
t5=(1,2,3,4,5,6,7,(1,2,3,4))
print(t5[-1][2])
#print(t5)  

#Editing items
'''t5[5]=10 immutable just like strings
print(t5)'''

#Adding items
t6=(1,2,3,4,5,6)
#t6[4]=5 #it's not possible

#Deleting items
t6=(1,2,3,4,5,6)
del t6
#print(t6)

# + and *
t7=(1,2,3,4,5)
t8=(5,6,7,8,9)
print(t7+t8) 
print(t7)
print(t8)
print(t7*3)
#mimbership
for i in t7:
    print(i)

#Tuple Function
#len/sum/max/min/sorted
t9=(1,2,3,4,5,6,1,1,3,2,5,3,2,)
print(len(t9))
print(sum(t9))
print(max(t9))
print(min(t9))
print(sorted(t9))   

# count
print(t9.count(1))
print(t9.count(5))
#index
print(t9.index(1))



a = [1,2,3]
b = a.copy()

a.append(4)
print(a)
print(b)

a = (1,2,3)
b = a

a = a + (4,)
print(a)
print(b)

a1=(1,2,3,4)
b1=a1

a1=a1+(10,)
print(a1)
print(b1)

#tuple unpacking
a,b,c=(1,2,3)
print(a)
print(b)
print(c)
d,e,*other=(1,3,9,5,4)
print(d)
print(e)
print(other)

a=1
b=2
print(a)
print(b)
a,b=b,a
print(a)
print(b)

# zipping tuples
a=(1,2,3,4)
b=(4,5,6)
print(tuple(zip(a,b)))

g=list(a)
g.append(10)
print(g)


