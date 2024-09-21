#list
#speed

a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
import time
start=time.time()
for i in range(len(a)):
  c.append(a[i]+b[i])

print(time.time()-start)  


#numpay
start=time.time()
import numpy as np
a=np.arange(10000000)
b=np.arange(10000000,20000000)

c=a+b
print(time.time()-start)

