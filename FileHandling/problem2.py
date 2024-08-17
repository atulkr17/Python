'''
Read through a text file, line by line. Use a dict to keep track of how many times each 
vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation 
-- dictionary.

'''

def count_vowel(filename):
    vowel=['a','e','i','o','u']
    dict={i:0 for i in vowel}
    for current_line in open(filename,'r'):
        for ch in current_line:
            if ch in dict:
               dict[ch]+=1
    return dict
vowel_count=count_vowel('F:\python10-07-24\Simple')    
print(vowel_count)