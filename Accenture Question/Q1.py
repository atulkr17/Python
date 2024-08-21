def AddCarry(num1,num2):

    total=num1+num2
    carry1=0

    while(total>0):
        listDigit=total%10
        ListDigit1=num1%10

        if listDigit < ListDigit1:
            carry1+=1

        total//=10
        num1//=10 

    return carry1


print('Total carry :-',AddCarry(451,349))
