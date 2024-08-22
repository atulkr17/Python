'''
Bank Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name 
(name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.
Eg. After making above classes and methods, on executing below code:-

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
Output:

Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹


'''
class BankAccount:

    def __init__(self,accno,name,balance):

     self.account=accno
     self.name=name
     self.balance=balance

    def  deposit(self):

       amount=int(input("Enter amount"))
       self.balance=self.balance+amount
       print(self.balance)
       print("Depositive successfuly")

    def  withdrawal(self):
       amount=int(input("Enter a amount"))
       if amount<self.balance:
          self.balance=self.balance-amount 
          reduction = self.bank_fees()
          self.balance=self.balance-reduction
          print("withdrawal successfully")

       else:
          print("amount is insufficent funds")
            
    def bank_fees(self):
       return 0.05 * self.balance      
        

    def display(self):
       print("Account holdar name",self.name) 
       print("Account number",self.account)
       print("Account balance",self.balance)  

obj=BankAccount(12345,'Atul kumar',2000000)  
obj.deposit()
obj.withdrawal()     
obj.display()
