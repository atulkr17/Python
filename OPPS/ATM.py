class ATM:
    # constructor(special function)->superpower -> 
    def __init__(self):
        self.pin=''
        self.balance=0

    def manu(self):
        user_input = input("""
        Hii how can i help you?
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to chake balance
        4. press 4 to withdraw
        5. Anything else  to exit                                                                                                                  
        """)  
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.Change_pin()
        elif user_input=='3':
            self.chake_bal()
        elif user_input=='4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):

        pin=input("Enter a new pin\n")
        self.pin=pin
        balance=int(input("Enter a amount\n"))
        self.balance=balance

        print("pin Create pin Successfully")
        self.manu()

    def Change_pin(self):
        old_pin=input("Enter old phone\n")    

        if old_pin==self.pin:
             # let him change the pin
            new_pin=input("Enter new pain\n")
            self.pin=new_pin
            print("pin change successfuly\n")
            self.manu()
        else:
            print("old pin was not correct\n")    
            self.manu()

    def chake_bal(self):
        user_pin=input("Enter a pin\n")
        if self.pin==user_pin:
            print("total bilance\n:-",self.balance)
            self.manu()    
        else:
            print("user pin is not valid\n")    
            self.manu()

    def withdraw(self):
        user_pin=input("Enter a pin number")
        if self.pin==user_pin:
            amount=int(input("Enter amount ") ) 
            if self.balance >= amount:
                self.balance=self.balance-amount
                print("withdraw seccessfuly",self.balance)
            else:
                print("your balance is unsificent")         
           
        else:
            print("wrong pin")

        self.manu()  
obj=ATM()
obj.manu()