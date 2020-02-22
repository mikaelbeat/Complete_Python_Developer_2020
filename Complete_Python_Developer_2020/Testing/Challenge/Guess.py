
import random


def guess_game(guess, random_value):
    if 0 < guess < 6:
        if guess == random_value:
            print("You guessed right!")
            return True
    else:
        print("Enter number between 1 -5!")
        return False

if __name__ == "__main__":
    
    random_value = random.randint(1, 5)

    while True:
        try:
            guess = int(input("Guess number between 1 - 5: "))
            if (guess_game(guess, random_value)):
                break
        except ValueError:
            print("Please enter a number!")
            continue