'''
Build flashcard using class in Python.
Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in 
memoization. Flashcards usually have a question on one side and an answer on the other.

Example 1:

Approach:

Create a class named FlashCard.
Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., 
{"Banana": "yellow", "Strawberries": "pink"}
Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong.
Output:

welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1

'''
import random

class FlashCard:

    def __init__(self):
        self.fruits={
            'apple':'red',
            'banana':'yellow',
            'watermelon':'green',
            'strawberry':'pink',
            'guava':'green'
        }

    def quiz(self):
        while True:

            #fruit,colour=random.choice(list(self.fruits.items()))[0]
            fruit,colour = random.choices(list(self.fruits.items()))[0]

            print('what is the colour of {}'.format(fruit))
            user_answer=input()

            if user_answer.lower()==colour:
                print("sahi jawab")

            else:
                print("galat jawab")

            option=int(input("Enter 0 to play again 1 to exit"))

            if option:
                break    

print('Welcome to the fruit quiz')
fc = FlashCard()
fc.quiz()

