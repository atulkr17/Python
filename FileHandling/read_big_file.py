with open('big.txt','r') as f:

    chuk_size=10

    while len(f.read(chuk_size))> 0:
        print(f.read(chuk_size),end='')
        f.read(chuk_size)