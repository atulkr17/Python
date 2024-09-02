def Binary_search(l):
    left,right=0,len(l)-1
    
    x=7
    while(left<=right):
        mid=(left+right)//2 
        if l[mid]==x:
            return mid
        elif l[mid]<x:
             left=mid+1
        else:
            right=mid-1
    return -1          
         

l=[1,2,3,4,5,6,7,8,9]
print(Binary_search(l))