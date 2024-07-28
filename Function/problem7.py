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
    #print(d)        
    max_value=(max(d.values()))

    for i in d:
        if d[i]==max_value:
            print(i,'->',max_value)
            break
s = 'hello how are you i am fine thank you' 
most_used(s)  