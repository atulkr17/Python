d={
    'Atul':'Bihar',
    'Amitesh':'Bihar',
    'Honey':'Bihar',
    'S.K.P':'UP',
    'Raj shree':'Bihar',
    'Avigya':'Jharkhand',
    'Anoushka':'Jharkhand',
    'Sutapa':'Bangladesh 😀'
}
with open('simpleFile','w') as f:
    f.write(str(d))
with open('simpleFile','r') as f:
    print(f.read())