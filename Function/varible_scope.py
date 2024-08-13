def f(y):
    y=y+1
    print("local varible",y)
y=7    
f(y)    
print('glole varible',y)


def f(y):
    x=x+1
    print("local varible",y)
x=7    
f(x)    
print('glole varible',x)