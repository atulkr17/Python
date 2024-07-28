
a=1
b=1
print(a)
print(b)
def fibb(n):
    global a,b
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fibb(7)        


