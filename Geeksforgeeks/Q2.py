def reverseSubArray(arr,l,r):

    l-=1
    r-=1

    while(l<r):
        arr[l],arr[r]=arr[r],arr[l]

        l+=1
        r-=1
    return arr    

# [1, 2, 3, 4, 5, 6, 7] and L = 2 and R = 4

print(reverseSubArray([1, 2, 3, 4, 5, 6, 7],2,4))