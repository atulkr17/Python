'''
 You are given a list of integers. 
 You are asked to make a list by running through elements of the list by adding all
 elements greater and itself.
i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

For 1st element 2 ->> these are greater (4+6+10)
 values and 2 itself so on adding becomes 22.

For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

like wise for all other elememts.

[2,4,6,10,1]-->[22,20,16,10,23]

'''
list1=[2,4,6,10,1]
list2=[]
for i in list1:
    sum=0
    for j in list1:
        if i<=j:
            sum=sum+j
    list2.append(sum)
print(list2)    
