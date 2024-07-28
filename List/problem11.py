'''
Write a program that can perform union operation on 2 lists
Example:

Input:

[1,2,3,4,5,1]
[2,3,5,7,8]
Output:

[1,2,3,4,5,7,8]

'''

a=[1,2,3,4,5,1]
b=[2,3,5,7,8]
union=[]

for i in a:
    if i not in union:
        union.append(i)
for j in b:
    if j not in union:
        union.append(j)
print(union)        
