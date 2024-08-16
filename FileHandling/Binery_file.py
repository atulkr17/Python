'''
with open('F:\python10-07-24\FileHandling\Photo.jpg','r') as f:
    print(f.read())
'''

with open("F:\python10-07-24\FileHandling\Photo.jpg",'rb') as f:
    with open('F:\python10-07-24\FileHandling\Photo1.jpg','wb') as wb:
        wb.write(f.read())