import sys
import random

target_number = random.randint(1, 100)
minimum_number = 1
maximum_number = 100

while True:
    guess = int(input(f"Please guess a number between {minimum_number} and {maximum_number}: "))
    if guess == target_number:
        print("Congratulations! You guessed the number!")
        sys.exit()
    elif guess < target_number:
        if guess < minimum_number:
            print("That is not a valid guess.")
        else:
            print("Your number is too low.")
            minimum_number = guess + 1
    elif guess > target_number:
        if guess > maximum_number:
            print("That is not a valid guess.")
        else:
            print("Your number is too high.")
            maximum_number = guess - 1
