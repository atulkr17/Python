def printnumber20(num):
  i=0
  while True:
    try:
        num+=1
        i+=1
        if i==21:
          raise StopIteration
    except StopIteration:
         break 
    else:
        print(num,end=' ')   
printnumber20(101)     