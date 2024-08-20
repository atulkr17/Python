def My_decorators(func):
    def wrriper():
        print("**********************")
        func()
        print("***********************")
    return wrriper
@My_decorators
def display():
    print("hii Atul") 


display()
     