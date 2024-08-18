'''
File Handling with Exception handling
Write a program that opens a text file and write data to it as "Hello, Good Morning!!!"
. Handle exceptions that can be generated during the I/O operations. Do not show the
 success message on the main exception handling block (write inside the else block).

'''

try:
    with open("text_file.txt", "w") as f:
        f.write("Hello, Good Morning!!!")
except IOError:
    print("Error working with file...")
else:
    print("File written successfully")