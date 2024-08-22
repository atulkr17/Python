'''

Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for
 this method.

Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as 
parameter for this method.

Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they
 have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method 
to display all the integer multiplication tables 1, 2, 3, ..., 9.

Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method
 that gets all the prime divisors of a given integer.

'''

class Computation:
    def __init__ (self):
        pass
# --- Factorial ------------
    def factorial(self, n):
        j = 1
        for i in range (1, n + 1):
            j = j * i
        return j
    
# --- Sum of the first n numbers ----
    def naturalSum(self, n):
        j = 1
        for i in range (1, n + 1):
            j = j + i
        return j
    
# --- Primality test of a number ------------
    def testPrime(self, n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False

# --- Primality test of two integers ------------
    def testPrims(self, n, m):
        
        # initialize the number of commons divisors
        commonDiv = 0
        for i in range (1, n + 1):
            if (n% i == 0 and m% i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print ("The numbers", n, "and", m, "are co-primes")
        else:
            print ("The numbers", n, "and", m, "are not co-primes")

#---Multiplication table-------------
    def tableMult(self, k):
        for i in range (1,10):
            print (i, "x", k, "=", i * k)

# --- All multiplication tables of the numbers 1, 2, .., 9
    def allTables(self):
        for k in range (1,10):
            print ("\nthe multiplication table of:", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)

# ----- list of divisors of an integer
    def listDivisor(self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0):
                lDiv.append (i)
        return lDiv

# ------ list of prime divisors of an integer ----------------
    def listPrimeDivisor(self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0 and self.testPrime(i)):
                lDiv.append(i)
        return lDiv

# Instantiation example
Comput= Computation ()
Comput.testPrims(13, 7)
print ("List of divisors of 18:", Comput.listDivisor(18))
print ("List of prime divisors of 18:", Comput.listPrimeDivisor(18))
Comput.allTables()
