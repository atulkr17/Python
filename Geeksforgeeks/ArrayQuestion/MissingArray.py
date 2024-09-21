def missingNumber( n, arr):
        
        # code here
        expectsum=int(n*(n+1)/2)
        actulsum=sum(arr)
        return expectsum-actulsum

print("missing number is ",missingNumber(5,[1,2,3,5]))