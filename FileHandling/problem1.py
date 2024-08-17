'''
Write a function get_final_line(filename), which takes filename as input and return final line
of the file.
Note: You can choose any file of your choice.

'''
def get_final_line(filename):

    list_line=''
    for Current_line in open(filename,'r'):
        list_line=Current_line
    return list_line
last_line=get_final_line('F:\python10-07-24\Simple')   
print(last_line) 