'''
Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.

List of Coordinates
[(1,1),(2,2),(3,3),(4,4)]
Query Point
(0,0)
Output
Nearest to (0,0) is (1,1)

'''

def shorted_dest(point,query):
    temp=[]
    for i in point:
        distance=((i[0] - query[0])**2 + (i[1] - query[1])**2)**0.5
        temp.append(distance)
    return point[sorted(list(enumerate(temp)),key=lambda x:x[1])[0][0]]
        

    
point=[(1,1),(2,2),(3,3),(4,4)]
query=(0,0)
print(shorted_dest(point,query))
