class A:

    def __init__(self):
        print("A init")
        

    def feture1(self):
        print("feture 1 working")
    def feture2(self):
        print("feture 2 working")
class B(A):
    def __init__(self):
       super().__init__()
       print("B init")

    def feture3(self):
        print("feture 3 working")
    def feture4(self):
        print("feture 4 working")

d=B()     
'''d.feture1() 
d.feture2() 
d.feture3() 
d.feture4()''' 
      
