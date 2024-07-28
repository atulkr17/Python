'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

'''
def even_number(a):
    result=[]
    for i in a:
        if i%2==0:
            result.append(i)
    return result        




l=[1, 2, 3, 4, 5, 6, 7, 8, 9]

c=even_number(l)
print(c)