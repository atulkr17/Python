import json

dec={'name':'Atul','list':[1,2,3,4,5,6]}

with open('demo.jhon','w') as f:
    json.dump(dec,f)
    
