'''
Q4. Create line wise reverse of a file
    Write a function which takes two arguments: the names of the input file
    (to be read from) and the output file (which will be created).

For example, if a file looks like

abc def
ghi jkl
then the output file will be

fed cba
lkj ihg
Notice: The newline remains at the end of the string, while the rest of the
 characters are all reversed.

'''

inputfile='F:\python10-07-24\Simple'
outputfile='F:\python10-07-24\simpel'

def reverse_str(infilename,outfilename):
   with open(infilename,'r') as infile, open(outfilename,'w') as outfile:
      for one_line in infile:
         outfile.write(one_line.rstrip()[::-1]+'\n')
        
reverse_str(inputfile,outputfile)        


