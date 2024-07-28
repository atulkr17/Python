from array import *


''' val = array('i',[12,3,4,5])



print(val)'''

arr=array("i",[])

n=int(input("enter a number"))

for i in range(n-1):
    x=int(input("Enetra a value"))
    arr.append(x)
print(arr)    

val=int(input("Enter a number which u want to search"))

k=0
for i in arr:
    if i==val:
        print(k)
        break
    k+=1    
else:
    print('number not present in tha array')    
