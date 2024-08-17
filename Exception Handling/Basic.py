try:
    with open('F:\python10-07-24\Simple','r') as f:
        print(f.read())
        print(m)
        print(5/0)
except FileNotFoundError:
    print("file not exit")        
except NameError:
    print("varible is not defne") 
except ZeroDivisionError:
    print("can't divde with 0")   
except Exception as e:
    print(e)            
