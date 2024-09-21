def diffcount(n,n1):
    i=len(n)-1
    j=len(n1)-1
    count=0
    while(i>0):
        if n[i]!=n1[j]:
            count+=1
            i-=1
        else:
            i-=1   
            j-=1      


    return "Even" if count%2==0 else "Odd",count

n='He ll o worl d'
n1='Hello world'

print(diffcount(n,n1))