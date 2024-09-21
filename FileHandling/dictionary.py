import json
d={
    'Atul':'Bihar',
    'Amitesh':'Bihar',
    'Honey':'Bihar',
    'S.K.P':'UP',
    'Raj shree':'Bihar',
    'Avigya':'Jharkhand',
    'Anoushka':'Jharkhand',
    'Sutapa':'Bangladesh '
}
with open('temp.tax','w') as f:
   c=json.dump(d,f,indent=4)

print(type(c))   

