
''' 
 You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of sum of elements.
List have elemnts as any no of key-pair dict with key as list index and value as any integer, integers and numeric-strings. There is always only one element in the dict.

l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])



'''


# Write code here
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
  try:
    s+=l[i]
  except TypeError as t:
    try:
      s+=l[i].get(i)   
    except AttributeError as a:
       s+=int(l[i]) 
print(s)      