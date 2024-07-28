a=int(input("Eenter a number u want to chake plendrom or not"))
rev=a
pl=0    
while a!=0:#153
    dig=a%10
    pl=pl*10+dig
    a=a//10
if(rev==pl):
    print("This is plendrom number:")
else:
    print("This is not plindrom number:")    


