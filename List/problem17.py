def resu(l):
    for i in l:
        if isinstance(i,list):
            resu(i)
        else:
            lst1.append(i)
lst1=[]
Lst = [1, 2, 3, [4, 5], [6, 7, 8], [9, [10]]] 
resu(Lst)  
print(lst1)
