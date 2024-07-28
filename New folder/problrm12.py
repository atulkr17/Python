'''Write a program to print whether a given number is a prime number or not'''
num=int(input("Enter a nuber"))
flag=0
for i in range(2,num):
    if num%i==0:
      flag=1
      break
if flag==0:
   print("prime number")
else:
   print("not prime number")      