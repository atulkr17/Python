class student:

    s=0
    '''def sum(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s'''
    def sum(a,b):
        s=a+b
    def sum(a):
        s=a    
    

d=student()


#print(d.sum(1,2,3))

print(d.sum(1,2))

print(d.sum(1))                
    