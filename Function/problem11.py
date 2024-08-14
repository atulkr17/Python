#Write a Python program to add three given lists using Python map and lambda.

l=[1,2,3,4,5]
l2=[4,3,2,8,0]
l3=[8,4,2,9,7]
l4=[8,4,2,8,9]

a=list(map(lambda a,b,c,d:a+b+c+d,l,l2,l3,l4))

print(a)