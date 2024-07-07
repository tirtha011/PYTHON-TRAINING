'''
OOP Guess my number game
Design and code the "guess my number game" using Object Oriented Programming.
Create a class called guessMyNumber and declare appropriate instance variables.
Create the run function and other relevant functions for completing the class.
P1 = guessMyNumber(“Ram”)
P1.run()
Sample Run:
Computer chooses a number between 1 and 100
You will have 10 attempts to guess the correct number
-> 10
Incorrect. Guess Higher
-> 50
Incorrect. Guess Lower
-> 30
Incorrect. Guess Higher
-> 40
Incorrect. Guess Higher
-> 45
Correct. Congratulations!
Good playing!: OOP Guess my number game
Design and code the "guess my number game" using Object Oriented Programming.
Create a class called guessMyNumber and declare appropriate instance variables.
Create the run function and other relevant functions for completing the class.
P1 = guessMyNumber(“Ram”)
P1.run()
Sample Run:
Computer chooses a number between 1 and 100
You will have 10 attempts to guess the correct number
-> 10
Incorrect. Guess Higher
-> 50
Incorrect. Guess Lower
-> 30
Incorrect. Guess Higher
-> 40
Incorrect. Guess Higher
-> 45
Correct. Congratulations!
Good playing!

'''

import random
class GuessMyNumber:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def run(self):
        print("Computer chooses a number between 1 and 100")
        print("You will have 10 attempts to guess the correct number")

        while True:
            guess = input("Enter your guess: ")

            try:
                guess = int(guess)
            except ValueError:
                print("Incorrect Please enter another number.")
                continue

            self.guesses += 1

            if guess == self.number:
                print("Correct. Congratulations!".format(self.guesses))
                print("Good playing!")
                break
            elif guess < self.number:
                print("Incorrect. Guess Higher ")
            else:
                print("Incorrect. Guess Lower ")

if __name__ == "__main__":
    game = GuessMyNumber()
    game.run()