'''
Check is tuples are same or not?
Two tuples would be same if both tuples have same element at same index

t1 = (1,2,3,0)
t2 = (0,1,2,3)

t1 and t2 are not same

'''
t1 = (1,2,3,0)
t2 = (0,1,2,3)
flage=True
for i,j in zip(t1,t2):
    if i==j:
        continue
    else:
        flage=False
        break
if flage:
    print("same")
else:
    print("not same")        
