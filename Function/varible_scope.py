def f(y):
    y=y+1
    print("local varible",y)
y=7    
f(y)    
print('global varible',y)


#this code is not run becouse you cannot increment global varible in function
'''def f(y):
    x=x+1
    print("local varible",y)
x=7    
f(x)    
print('global varible',x)'''

#you can access through Globle keyword
def f(y):
    global x
    x=x+1
    print("local varible",y)
x=7    
f(x)    
print('glole varible',x)


def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')