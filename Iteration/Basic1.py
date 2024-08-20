#Example

import sys
l=[1,2,3,4,5,6,7]

l=[i*2 for i in l]
print(l)

l1=[x for x in range(1,10000000)]
print("first time complicity")
print(sys.getsizeof(l1)/64)
print("Both range is same this is magic of iterator")
gen=range(1,1000000000)
print("Second time complicity")
print(sys.getsizeof(gen)/64)