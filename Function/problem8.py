'''
Write a python function that receives a list of integers and prints out a histogram of bin size 10

Input:
[13,42,15,37,22,39,41,50]
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}

'''
import math
def hestogram(l):

    d={}
    min_value=math.floor(min(l)/10)*10
    max_value=math.ceil(max(l)/10)*10

    for i in range(min_value,max_value,10):
        count=0
        for j in l:
            if i+1<=j<=i+10:
                count+=1
        d[str(i+1)+ '-' +str(i+10)]=count
    return d            



l=[13,42,15,37,22,39,41,50]    
print(hestogram(l))




