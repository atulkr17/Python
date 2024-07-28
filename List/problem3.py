'''
Update no of items available
Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -
input
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

output
Jelly Belly-10
Kit Kat-20
Double Bubble-34
Milky Way-74
Three Musketeers-32

'''
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
for (i,j) in zip(candy_list,no_of_items):
    print(i,'-',j)