''': Write a program that take a user input of three angles
 and will find out whether it can form a triangle or not.
Hint - Sum of all angles is 180 and all angles are positive'''

num=int(input("Enter a first number"))
num1=int(input("Enter a second number"))
num2=int(input("Enter a third number"))

if(num+num1+num2)==180 and num>0 and num1>0 and num2>0:
    print("fron is tengular")
else:
    print("doesnot from is tengular")    
