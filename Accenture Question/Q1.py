def Addcarry(num1,num2):
    total=num1+num2
    carry=0
    while(total > 0):
        listDigit=total%10
        listdigit1=num1%10
        if listDigit < listdigit1:
            carry+=1

        total=total//10 
        num1=num1//10   
        
    return carry

print(Addcarry(451,349))