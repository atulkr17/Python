def rede(list1):
    
    for i in list1:
        if isinstance(i,list):
            rede(i)
        else:
            temp.append(i)
   
temp=[]            
list1=[1,2,3,[4,5],[6,7,8],[9,[10]]]
rede(list1)
print(list1)
print(temp)