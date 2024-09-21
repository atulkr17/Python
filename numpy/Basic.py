import numpy as np
# np.array
a=np.array([1,2,3,4,5,6,7])
print(a)

#np.array 2d and 3d

a=np.array([[1,2,3,4],[1,4,3,2],[1,2,3,4]])
print(a)


# dtype

a=np.array([1,2,3,4,5], dtype=float)
print(a)

#np.arange
a=np.arange(16).reshape(4,4)
print(a)


# np.ones and np.zeros
a=np.ones((3,7))
print(a)

b=np.zeros((3,7))
print(b)


# np.random

a=np.random.random((3,4))
print(a)

## np.linspace
a=np.linspace(-10,10,10)
print(a)

# np.identity
a=np.identity(7)
print(a)


#Array Attributes

a = np.arange(10,dtype=np.int32)
b=np.arange(12,dtype=float).reshape(3,4)
c=np.arange(8).reshape(2,2,2)


# ndim
print(a.ndim)
print(b.ndim)
print(c.ndim)

# shape
print(c.shape)

# size
print(a.size)

# itemsize
print(c.itemsize)



a1=np.arange(12).reshape(3,4)
print(a1)

#print(a1[1::2,0::3])
print(a1[:2,1:])



b1=np.arange(27).reshape(3,3,3)
print(b1)

#iteroter
b=np.array([1,2,3,4,5,6,7])
for i in b:
    print(i)

c=np.arange(12).reshape(3,4)    
print(c)
for i in 

