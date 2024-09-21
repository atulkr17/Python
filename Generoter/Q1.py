def Fibo(item):
    a,b=0,1
    while(b<item):
        yield b
        a,b=b,a+b
print("0")        
for i in Fibo(200):
    print(i)