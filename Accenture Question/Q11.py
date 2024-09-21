def DectoNBase(n,num):
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result=[]

        while(num>0):
                reminder=num%n
                result.append(symbols[reminder])
                num//=n

        return "".join(result)    


   


print(DectoNBase(12, 718)) 