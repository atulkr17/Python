def Roman(num):

    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]

    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

    result=" "

    for i in range(len(number)):
        while num >= number[i]:
            result+=roman[i]
            num-=number[i]
    return result

print(Roman(19900))        
        
       
        
        
    
    
   
    