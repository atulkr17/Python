'''
 Write a python function that accepts a string as input and returns the word with most occurence.

Input:
hello how are you i am fine thank you
Output
you -> 2

'''

def most_used(s):
    d={}
    for i in s.split():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    max_no = max(d.values())
    for i in d:
        if d[i]==max_no:
            print(i,'->',d[i])
            break



most_used('hello how are you i am fine thank you') 