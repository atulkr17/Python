'''
Create a text file (using an editor, not necessarily Python) containing two tab 
separated columns, with each column containing a number. Then use Python to read 
through the file you’ve created. For each line, multiply each first number by the 
second and include it in the file in third column. In last add a line Total, by 
summing the value of third column
Input File example: That you need to create

1   2
3   4
5   6
7   8
9   10
Output File Example:

1   2   2
3   4   12
5   6   30
7   8   56
9   10  90
Total   190

'''

filename='test-2.txt'
f=open(filename,'w')
for i in range(1,11,2):
    line='{}\t{}\n'.format(i,i+1)
    f.write(line)
f.close()

with open(filename,'r') as f:
   lines=f.read().splitlines()
total=0
with open(filename,'w') as f:
    for line in lines:
        a,b=line.split(sep='\t')
        res=int(a) * int(b)
        total+=res
        add='{}\t{}\t{}\n'.format(a,b,res)
        f.write(add)
    f.write('total\t'+str(total))    