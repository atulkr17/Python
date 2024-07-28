#Q what is list??
#-->list is heterogeneous data type,it's mutable, non-unique data structure. and list is denoted by square bracket

#Q why we use list in python
#-->Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data


list=['Atul','kumar','ankush','kumar','rajeevranjan','sharma']
#print all data in list
print(list)

#To determine how many items a list has, use the **len()** function:
print(len(list))

print(list[:2])
print(list[3])

#Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"] #Note: The first item has index 0.
print(thislist[1])


#Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


'''Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:3])
print(thislist[2:])


#Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-0])


#To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
#s=input("enter a stering")
# if s in thislist:
if 'apple' in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("item not present in the list")  


#To change the value of a specific item, refer to the index number:
list=[1,2,3,4,5,6,7]
#print(list)
list[1]=19
#print(list)

#Change the values "2" and "3" with the values "12" and "13":
list[1:2]=[12,13]
print(list)
list[1:6]=[2,5] # this part didn't understand vary well
print(list)



'''To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:'''

thislist = ["apple", "banana","mango","papaya","cherry"]
thislist.insert(2,'Atul')
print(thislist)
thislist.insert(3,'blackbary')
print(thislist)

#To add an item to the end of the list, use the append() method:
thislist = ['apple', 'banana', 'Atul', 'blackbary', 'mango', 'papaya', 'cherry']
thislist.append("orange")
print(thislist)


#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#The extend() method does not have to append lists, 
#you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The remove() method removes the specified item.
thislist =  ['apple', 'banana', 'Atul', 'blackbary', 'mango', 'papaya', 'cherry']
thislist.remove("Atul")
print(thislist)

#The pop() method removes the specified index.
thislist.pop()#Remove the last item:
print(thislist)

thislist.pop(1)
print(thislist)

#The del keyword also removes the specified index:
del thislist[1]


'''The del keyword can also delete the list completely.
del thislist()
print('yes del function',thislist)# this function is not working
'''
#The clear() method empties the list.
#The list still remains, but it has no content.
thislist.clear()
print(thislist,'list is empty')


list2=[1,2,3,4,5,1,2,2,2,]
print(list2)

