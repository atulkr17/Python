def list1(num):
    for i in num:   
      if isinstance(i,list):
         list1(i)
      else:
         l3.append(i)
    return l3    
L2 = [5,6,7,8,[1,2,3,4,[5,3,2]]]
l3=[]           
print(list1(L2))
print(l3)