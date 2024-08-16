d={
    'Atul':'bihar',
    'Amitesh':'bihar',
    'Honey':'Bihar',
    'S.K.P':'UP',
    'XYZ':'bihar',
    'Avigya':'jharkhand',
    'Anoushka':'jharkhand',
    'Sutapa':'Bangladesh '
}
with open('simpleFile','w') as f:
    f.write(str(d))
with open('simpleFile','r') as f:
    print(f.read())