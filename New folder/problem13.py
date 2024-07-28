'''Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. 
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.'''
start=int(input("Enter first number"))
end=int(input("Enter second number"))

for num in range(start,end+1):
    temp=num
    temp1=num
    count=0
    sum=0
    '''while(temp!=0):
        c=temp%10
        count+=1
        temp=temp//10'''
    order = len(str(num))
    while(temp1!=0):
        digit=temp1%10
        sum=sum+digit**order
        temp1=temp1//10
    if num==sum:
        print(num)        


