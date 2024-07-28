'''
Write a Python function that accepts a hyphen-separated sequence of words as 
parameter and returns the words in a hyphen-separated sequence after 
sorting them alphabetically.
Example 1:

Input:

green-red-yellow-black-white
Output:

black-green-red-white-yellow

'''
def sore_sequence(seq):
    temp=[]
    for i in sorted(seq.split('-')):
        temp.append(i)
    return '-'.join(temp)    

s='green-red-yellow-black-white'
print(sore_sequence(s))