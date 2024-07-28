'''
Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List
input
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

output
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print('Befour addind 7000',list1[2][2])
list1[2][2].append(7000)
print("After adding 7000",list1)