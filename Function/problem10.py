'''
Write a python program that receives a list 
of strings and performs bag of word operation on those strings
L = [
    'cat mat rat cat',
     'sat bat fat cat rat',
     'pat cat mat rat'
]
'''
def bow(l):
    vacab=set()

    for i in l:
        vacab.update(i.split())
    result=[]
    print(vacab)

    for i in l:
        result.append([])
        for j in vacab:
            result[-1].append(i.count(j))
    return result        

l = [
    'cat mat rat cat',
     'sat bat fat cat rat',
     'pat cat mat rat'
]
print(bow(l))