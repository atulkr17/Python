'''Combine two lists index-wise(columns wise)
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item from both the list,
 then the 1st index item, and so on till the last element.
   any leftover items will get added at the end of the new list.
input
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
output
[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
'''
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
'''

for i in list1:
    for j in list2:
        b=list(zip(list1,list2))
print(b)      
'''
list3=[[i,j] for (i,j) in zip(list1,list2)]
print(list3)