def mul(a,b):

    if b==1:
        return 1
    else:
        return a + mul(a,b-1)
print(mul(5,4))    