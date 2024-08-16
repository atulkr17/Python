'''
Using Context Manager (With)
It's a good idea to close a file after usage as it will free up the resources
If we dont close it, garbage collector would close it
with keyword closes the file as soon as the usage is over

'''

with open('F:\python10-07-24\Simple','w') as f:
   f.write("hii how are you \n i am find \n what about you")