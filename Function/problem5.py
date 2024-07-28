'''
Write a Python function to check whether a number is perfect or not.
A Perfect number is a number that is half the 
sum of all of its positive divisors (including itself).

Example :

The first perfect number is 6, because 1, 2, and 
3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
Equivalently, the number 6 is equal to half
 the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
 This is followed by the perfect numbers 496 and 8128.


'''
def perfect_number(p):
    sum=0
    for i in range(1,p):
        if p%i==0:
            sum=sum+i
    return sum        


a=int(input("Enter a number"))
c=perfect_number(a)
if a==c:
    print("perfect number")
else:
    print("not perfect number")    