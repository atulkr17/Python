'''
Write a number game program. Ask the user to enter a number. If the number is greater 
than number to be guessed, raise a ValueTooLarge exception. If the value is smaller 
the number to be guessed the, raise a ValueTooSmall exception and prompt the user to
enter again. Quit the program only when the user enters the correct number. Also 
raise GuessError if user guess a number less than 1.

'''
import random
class ValueTooLarge(Exception):
    def display(self):
        print("input number is large")
class ValueTooSmall(Exception):
    def display(safe):
        print("input number is small")
class GuessError(Exception):
    def display(self):
        print('Guess error')

num=random.randint(1,100)
print('computer guess number',num)
while 1:
    
  
    try:
        guess=int(input('inter a number'))
        if guess<1:
            raise GuessError
        elif guess > num :
            raise ValueTooLarge
        elif guess <num:
            raise ValueTooSmall
        elif guess==num:
            print('Great You succeeded...')
            break
    except GuessError as g:
        g.display()
    except ValueTooLarge as v:
        v.display()  
    except ValueTooSmall as v1:
        v1.display()
              