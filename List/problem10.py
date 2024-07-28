'''
Add Space between Potential Words.
Example:

Input:

['campusxIs', 'bestFor', 'dataScientist']
Output:

['campusx Is', 'best For', 'data Scientist']

'''
l=['campusxIs', 'bestFor', 'dataScientist']
r=[]
for i in l:
    temp=[[]]
    for char in i:
        if char.upper():
            temp.append([])

        temp[-1].append(char) 
    #print(temp)       
    temp_string=""
    for item in temp:
        temp_string=temp_string+''.join(item)+''
    r.append(temp_string[0:-1])
print(r)        

