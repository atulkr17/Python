class point:

    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
        
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origen(self):
        return (self.x_cod**2 + self.y_cod**2)**0.5
          
class line:

    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
         

    def __str__(self):
        return '{}x + {}y +{} = 0'.format(self.A,self.B,self.C)
    
    def point_on_the_line(line,point):

        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return ' lies on the line '
        else:
            return 'does not lies on the line'
        
    def shortest_distance(line,point):

       return abs(line.A*point.x_cod + line.B*point.y_cod + line.C) /(line.A+line.B)**2
                  
'''
p=point(1,2)
p1=point(2,4)
#print(p.euclidean_distance(p1))
print(p.distance_from_origen())
'''
l=line(1,1,-2)
p1=point(1,1)
print(l.shortest_distance(p1))