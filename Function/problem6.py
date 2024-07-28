'''
Write a Python function to concatenate any no of dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''
def merge_dict(*kwarge):
    d1={}
    for i in kwarge:
        d1.update(i)
    return d1    


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

One_dict=merge_dict(dic1,dic2,dic3)
print(One_dict)