l=['hello word'for i in range(10000)]

with open("big.txt",'w') as f:
    f.writelines(l)

