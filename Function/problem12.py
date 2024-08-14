'''
Write a Python program to create a list containing the power of said number
 in bases raised to the corresponding number in the index using Python map.

'''
list1 = [1,2,3,4,5,6]
'''
list=[]
for i in range(len(list1)):
    a=list1[i]**i
    list.append(a)
print(list)'''
a=(list(map(lambda a,b:a**b,list1,range(len(list1)) ))  ) 
print(a) 
