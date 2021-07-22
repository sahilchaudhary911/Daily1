"""
Write a guessing game where the user has to guess a secret number.
After every guess the program tells the user whether their number was too large
or too small. At the end the number of tries needed should be printed.
It counts only as one try if they input the same number multiple times consecutively.
"""

import random


def guessing_game():
    secret_number = random.randint(0, 20)
    tries = 0
    while True:
        guess = int(input("Guess a number betwee 0 to 20: "))
        tries += 1
        if guess == secret_number:
            print(f"You guessed the correct number. Total tries = {tries}")
            return


guessing_game()
