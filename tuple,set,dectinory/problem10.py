'''

Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
Example 1:

Input:

lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
Output:

[9, 10, 4, 5]


'''
list1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
list2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

list=[item for item in list1 if item in list2]
print(list)