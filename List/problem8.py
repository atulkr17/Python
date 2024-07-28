'''
Split String of list on K character.

Example :

Input:

['CampusX is a channel', 'for data-science', 'aspirants.']
Output:

['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
[ ]


'''
list=['CampusX is a channel', 'for data-science', 'aspirants.']
n=' '
result=[]
for i in list:
    result.extend(i.split(n))
print(result)    
    