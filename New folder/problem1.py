'''Write a program that will give you in hand monthly salary after deduction
 on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%'''

num=int(input("Enter a number"))

if num<5000000:
    salary=num*.82
elif num < 1000000:
    salary=num*.72
elif num<2000000:
    salary=num*.62
else:
    salary=num*.52    
print("You in hand monthly salary will be-", round(salary/12,2))    
