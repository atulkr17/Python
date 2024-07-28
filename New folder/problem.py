''' Write a program that keeps on accepting a number
 from the user until the user enters Zero. 
 Display the sum and average of all the numbers.
[ ]
'''
sum=0
count=0
while True:
    num=int(input("Enter a number"))
    if num==0:
      break
    sum=sum+num
    count=count+1
print(sum)
print("averaje number",sum/count)    