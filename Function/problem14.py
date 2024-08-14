# Use reduce to convert a 2D list to 1D
import functools
list2 = [[1, 2, 3],
        [3, 6, 7],
        [7, 5, 4]]

l=functools.reduce(lambda x,y:x+y,list2)
print(l)



def rede(list1):
    temp=[]
    for i in list1:
        if isinstance(i,list):
            rede(i)
        else:
            temp.append(i)
    return temp
            
list1=[1,2,3,[4,5],[6,7,8],[9,[10]]]
print(list1)
print(rede(list1))