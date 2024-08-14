'''
Using filter() and list() functions and .lower() method
 filter all the vowels in a given string.

 input:-"FIFA world cup in 2022 will take place in Qatar"

'''
str="FIFA world cup in 2022 will take place in Qatar"

a=list(filter(lambda a:True if a.lower() in'aeiou' else False,str))
print(a)
