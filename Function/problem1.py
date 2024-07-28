'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Exercise 1:

Input:

[1,2,3,3,3,3,4,5]
Output:

[1, 2, 3, 4, 5]

'''
def return_unique(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1        
l=[1,2,3,3,3,3,4,5]
a=return_unique(l)
print("Unique value", a)