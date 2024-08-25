'''
Find the area of a rectangle.
Approach:

The class name should be Rectangle.
The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
Create a method called area() which has no parameters.
Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
If you are using a if-else block inside the is_square() method, then use the one-linear syntax.

'''

class Rectangle:

    def __init__(self,l,b):
        self.length=l
       
        self.width=b
    
    @classmethod
    def property(self,len,ber):
        
        return  self(len,ber)
    
    def Area(self):
        return self.length*self.width
    
    def is_squer(self):
        return True if self.length==self.width else False
    
r=Rectangle.property(4,4)
print(r.Area())
print(r.is_squer())       
