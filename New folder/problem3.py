''' Write a program that will take user input of cost price and selling price
 and determines whether its a loss or a profit.'''

cost=int(input("Enter a number"))
selling=int(input("Enter a number"))

if cost<selling:
    print("profit")
elif cost >selling:
    print("losse")
else:
    print("no losse or no gain")        
