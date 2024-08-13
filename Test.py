#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#list1[2][2][1]=7000
#list1[2][2].append(70000)
#print(list1)
#print(list1[2][2][1])
#list=[4,1,6,2,4,9]
#for i in range(len(list)):
 #
 
#   print(i)
lst=[1,1,2,2,5,3,5,5]

l=[]
for i in lst:
    count =0
    for j in lst:
        if i==j:
            count+=1
    l.append(count)
print(l)    



