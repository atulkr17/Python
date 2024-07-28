'''
Write a list comprehension to print the following matrix
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
'''
list=[[j + 3*i for j in range(0,3)] for i in range(0,3)]
print(list)