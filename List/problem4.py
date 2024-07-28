'''
Running Sum on list
Write a program to print a list after performing running sum on it.

i.e:

Input:

list1 = [1,2,3,4,5,6]

Output:

[1,3,6,10,15,21]

'''
list1 = [1,2,3,4,5,6]
list2=[]
sum=0

for i in list1:
  sum=sum+i
  list2.append(sum)
print(list2)  
