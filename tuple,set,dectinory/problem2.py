'''
Multiply Adjacent elements (both side) and take 
sum of right and lest side multiplication result.
For eg.

The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication : 

(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

output-(5, 40, 91, 136, 80)
'''
l=(1, 5, 7, 8, 10)

result=[]
result.append(l[0]*l[1])
for i in range(1,len(l)-1):
    result.append(l[i]*l[i-1]+l[i]*l[i+1])
result.append(l[-1]*l[-2]) 
print(result)   
