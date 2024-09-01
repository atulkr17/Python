#find sum of the distinct (non repeating) element in array
 
l=[10,15,15,20,10,30]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1  
key=list(d.keys())
value=list(d.values())

sum=0
for i in range(len(d)):
    if value[i]==1:
        sum=sum+key[i] 
    else:
        pass
print("Distinct total number sum", sum)         


     