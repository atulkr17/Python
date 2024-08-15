# *args
# allows us to pass a variable number of non-keyword arguments to a function.


def multiply(*args):
    product=1
    for i in args:
        product=product * i
    return product
print(multiply(1,2,3,4,5,6,7,8,9))
     