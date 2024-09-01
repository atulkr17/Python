#find sum of the distinct (non repeating) element in array
l=[10,15,15,20,10,30]

sum1=sum([num for num in l if l.count(num)==1])
print('Distinct total number sum',sum1)