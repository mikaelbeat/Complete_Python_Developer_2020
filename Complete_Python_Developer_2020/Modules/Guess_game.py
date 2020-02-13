
import sys

from random import randint

value1 = int(sys.argv[1])
value2 = int(sys.argv[2])

random_value = randint(value1, value2)

print("\n********** GUESS GAME **********\n")

try:
    guess = int(input(f"\nGuess a number between {value1} - {value2}: "))
except ValueError:
    print("\nPlease enter only numeric values!")

while True:
    try:
        if guess > 0 and guess < 6:
            if guess == random_value:
                print("\nGreat job, you guessed right!")
                break
            else:
                print("\nWrong answer, try again!")
                guess = int(input(f"\nGuess a number between {value1} - {value2}: "))
        else:
            print(f"\nPlease enter only values between {value1} and {value2}")
            guess = int(input(f"\nGuess a number between {value1} - {value2}: "))
    except ValueError:
        guess = int(input(f"\nPlease enter only values between {value1} - {value2}: "))
        continue
