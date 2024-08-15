f=open('F:\python10-07-24\Atul1.txt','r')
while True:
        s=f.readline()

        if s== '':
            break
        else:
           print(s,end='')
f.close()           