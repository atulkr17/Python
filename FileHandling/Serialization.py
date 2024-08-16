import json

d={
    "Atul":"Bihar",
    "Amitesh":"Bihar",
    "Honey":"Bihar",
    "S.K.P":"UP",
    "Raj shree":"Bihar",
    "Avigya":"Jharkhand",
    "Anoushka":"Jharkhand",
    "Sutapa":"Bangladesh"
}

with open('SimpleFile','w') as f:
   json.dump(d,f)
    
