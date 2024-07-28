'''
Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:

['1ac21', '23fg', '456', '098d','1','kls']
Output:

['456', '23fg', '1ac21', '1', 'kls', '098d']

'''
L = ['1ac21', '23fg', '456', '098d','1','kls']
prod_value = []
for item in L:
  product = 1
  for char in item:
    if char.isdigit():
      product = product*int(char)

  prod_value.append(prod_value)
 

[i[1] for i in sorted(list(zip(product_list,L)),reverse=True)]

#i did not understand this code yet.
#this code is not running becoude something is wron in this code.