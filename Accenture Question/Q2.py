def lcp(st):
    str=st[0]
  
    for i in range(len(st)-1):

        first=str
        print(str)
        second=st[i+1]
        min_no=min(len(first),len(second))
        str=''

        for j in range(min_no):

            if first[j]==second[j]:
                str+=first[j]
            else:
                break
            
    return str            
 
s=["geeksforgeeks", "geeks", "geek", "geezer"]
print(lcp(s))