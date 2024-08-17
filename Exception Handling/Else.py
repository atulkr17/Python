try:
    f=open('Simple','r') 
except FileNotFoundError:
        print("file not find")
except NameError:
      print("name not exict")
else:
      print(f.read()) 
      f.close()             
