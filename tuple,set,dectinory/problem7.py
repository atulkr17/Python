'''
Write a program to count unique number of vowels using sets in a given string. 
Lowercase and upercase vowels will be taken as different.
Input:

Str1 = "hands-on data science mentorship progrAm with 
live classes at affordable fee only on CampusX"
Output:

No of unique vowels-6

'''

l=set("hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX")

vowels=set("aeiouAEIOU")

print("No of unique vowels-",len(vowels & l))