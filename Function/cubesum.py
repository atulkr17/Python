def cube1(f):
   return f**3

def cube(f,l):
    l1=[]
    for i in l:
        l1.append(f(i))
    return l1
def add(result):
    sum=0
    for i in result:
        sum=sum+i
    return sum      

l=[1,2,3,4,5,6,7,8,9]
cub=cube(cube1,l)
print(cub)
print(add(cub))