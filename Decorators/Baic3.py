def My_decorators(func):
    def wrriper():
        print("**********************")
        func()
        print("***********************")
    return wrriper

def display():
    print("hii Atul") 

a=My_decorators(display)
a()       