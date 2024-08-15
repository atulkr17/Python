# Use reduce to convert a 2D list to 1D
import functools
list2 = [[1, 2, 3],
        [3, 6, 7],
        [7, 5, 4]]

l=functools.reduce(lambda x,y:x+y,list2)
print(l)



