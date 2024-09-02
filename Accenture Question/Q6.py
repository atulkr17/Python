def Exponent(a,b):
    max_number=a
    max_exponent=0
    for i in range(a,b+1):
        num=i
        exponent=0
        while(num%2==0):
            num=num//2
            exponent+=1

        if max_exponent < exponent:
            max_exponent=exponent
            max_number=i
    return max_number        

print(Exponent(128,510))         
