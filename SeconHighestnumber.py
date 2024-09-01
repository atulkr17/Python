l=[1,2,3,4,4,5,5,5]
max=0
secmax=0

for i in range(len(l)):

    if max < l[i]:
        secmax=max
        max=l[i]

    elif secmax < l[i] and max > l[i]:
        secmax = l[i]

print(l.count(4))