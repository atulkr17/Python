import numpy as np


b1=np.arange(27).reshape(3,3,3)
print(b1)


print(b1[2,0::2,0::2])




b=np.ones((3,4),dtype=int)
print(b)