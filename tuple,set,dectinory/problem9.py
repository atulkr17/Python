'''
find union of n arrays.
Example 1:

Input:

[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]

 Output:

[1, 2, 3, 4, 5, 6, 7, 9]

'''
l=[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
l2=set()
for i in l:
    l2.update(i)
print(list(l2))    
