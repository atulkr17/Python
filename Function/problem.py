'''
 Write a python function that receives a list of integers and prints out a histogram of bin size 10

Input:
[13,42,15,37,22,39,41,50]
Output:
{11-20:2,21-30:1,31-40:2,41-50:3}

'''
import math
l=[13,42,15,37,22,39,41,50]
min_bin=math.floor(min(l)/10)*10
max_bin=math.ceil(max(l)/10)*10
d={}
for i in range(max_bin,max_bin,10):
    count=0
    for j in l:
        if 




#l=[13,42,15,37,22,39,41,50]