def maxthreeNoproduct(l):

    l1=sorted(l)
    s=len(l1)

    return l1[s-1]*l1[s-2]*l1[s-3]





l=[4,3,2,1]
print(maxthreeNoproduct(l))