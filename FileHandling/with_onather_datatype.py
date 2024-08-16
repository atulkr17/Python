'''
with open('simpel','w') as f:
    f.write(5)
'''
with open('simpel','w') as f:
    f.write('5')

with open('simple','r') as f:
    print(int(f.read())+5)  