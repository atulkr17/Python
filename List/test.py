import math
def Exponet(a,b):
    min=int(math.log2(a))
    max=int(math.log2(b))
    rem=a-(2**max%a)
    while max>0:
            if(2**max>=a and 2**max<=b):
                return 2**max
            elif 2**max<a and a+((2**max)%a-( rem))<b:
                 return a+((2**max)%a-(rem))
         

            max-=1
    return 0        

print(Exponet(66,123))    