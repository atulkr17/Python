'''
Join Tuples if similar initial element
While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

For eg.

Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

'''
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
unique=[]
for i in test_list:
    unique.append(i[0])
unique=set(unique)
#print(unique)  
result=[]
for i in unique:
   result.append([i])
   for j in test_list:
       if j[0]==i:
          result[-1].append(j[1])
print(list(map(tuple,result)))        

