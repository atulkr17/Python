''': Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit
Hint

1 cm = 0.032ft
1km = 0.62
1 USD = 80 INR'''

menu=int(input("Enter a number"))

if menu==1:
    cm=float(input("Enter a cm value"))
    print("cm value",cm*0.032)
elif menu==2:
    km=float(input("Enter a number"))
    print("km value",km*0.62)
elif menu==3:
    usd=float(input("enter a value"))
    print("usd value",usd*80)     
else:
    exit()       
