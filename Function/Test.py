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

def transform(f,l):
    output=[]
    for i in l:
        output.append(f(i))
    return output    
def sum(a):
    add=0
    for i in a:
        add=add+i
    return add    

L = [1,2,3,4,5]

a=transform(lambda x:x**3,L)
print(sum(a))