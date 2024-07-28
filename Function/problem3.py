'''
Write a Python function that accepts a string and calculate the number 
of upper case letters and lower case letters.
Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
Expected Output :
No. of Upper case characters :  9
No. of Lower case Characters :  47

'''
def lower_upper(s):
    lower_case=0
    upper_case=0
    for i in s:
        if i.islower():
            lower_case+=1
        elif i.isupper():
            upper_case+=1
        else:
            pass
    return lower_case,upper_case
            
s = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
x,y=lower_upper(s)
print("lower case",x)
print("upper case",y)