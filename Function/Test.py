'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers.count(2))
target = 5

number1=[]

for i in range(len(numbers)):
    num1=numbers[i]
    for j in range(i+1,len(numbers)):
        num2=numbers[j]
        if num1+num2==target:
            number1.append((num1,num2))
print(number1)  '''
l=[1,2,3,[4,5,5,[8,9,3,2],1]]
l1=[]
for i in range (len(l)):
    if isinstance(l[i],list):
        for j in (l[i]):
            l1.append(j)
    else:
        l1.append(l[i])  
print(l1)              

    

