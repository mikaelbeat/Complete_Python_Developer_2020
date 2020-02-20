
import random


def guess_game(guess):

    random_value = random.randint(1, 5)

    while True:
        try:
            #guess = int(input("Guess number between 1 - 5: "))

            if 0 < guess < 5:
                if guess == random_value:
                    print("You guesses right!")
                    break
            else:
                print("Enter number between 1 -5!")
        except ValueError:
            print("Please enter a number!")
            continue


#guess_game()