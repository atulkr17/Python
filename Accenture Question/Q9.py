def pair(l,s):
    l.sort()
    print(l)
    max=0
    x,y=0,0
    for i in range(len(l)-1,1,-1):
        for j in range(i):
            if l[i]+l[j]==s:
                if(max<l[i]*l[j]):
                    x,y=l[i],l[j]
                    max=l[i]*l[j]
                
    return x,y
            




l=[11,9,13,10,8,7,4,12]
s=18
print(pair(l,s))