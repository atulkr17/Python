# empty
s=set()
print(s)
print(type(s))
# 1D and 2D
s={1,2,3,4}
print(s)
s1={1,2,3,4,5,(6,7,8,9)}
print(s1)
print(type(s1))
#s1={1,2,3,{4,5,6}} // This  is not work in python
# using type conversion
g=set([1,2,3,4])
print(type(g))
# duplicates not allowed
s1={1,1,2,3,4,5,6,6}
print(s1)


# set can't have mutable items
#s={1,2,[3,4]}
print(s)

s={1,2,3}
s1={3,2,1}
print(s==s1)

#Accessing Items
s={1,2,3}
#print(s[0])//acessingh item is not possible in set

#Editing Items// Editing item is not possible in set becouse set is not working in indexing
# Adding item in set

s={1,2,3,4}
s.add(5)
print(s)
#update
s.update([6,5,8,9])
print(s)

#deleting item from set
s={1,2,3,4,'hello','atul'}
print(s)
s.remove(2)
print(s)
s.discard(20)
print(s)
s.pop()
print(s)
s.clear()
print(s)
del s



#Set Operation
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
#union(|)
print(s1|s2)
# Intersection(&)
print(s1&s2)
# Difference(-)
print(s1-s2)
# Symmetric Difference(^)
print(s1^s2)
# Membership Test
print(1 in s1)
# Iteration
for i in s1:
  print(i)


