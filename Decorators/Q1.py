def my_decoder(func):
    def wrapper():
         print("Something is happening before the function is called.")
         func()
         print('something is happening after the function call')   

    return wrapper

@my_decoder
def Say_hello():
     print("hello")    

Say_hello()           
