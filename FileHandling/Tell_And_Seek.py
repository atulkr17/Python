with open('simple','r') as f:
    print(f.read(5))
    print(f.tell())
    print(f.seek(2))
    print(f.read())