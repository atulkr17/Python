
import json
# list
l=[1,2,3,4,5]
with open('Simple4.tax','w') as f:
    json.dump(l,f)

#dict

d={
    'Atul':20,
    'Amitesh':21,
    'honey':22
}

with open('simple4.tax','w') as f:
    json.dump(d,f,indent=4)

#print(type(d))    

