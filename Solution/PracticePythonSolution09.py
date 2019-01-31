# Practice Python: Exercise 09
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random


def solution():
    var_number = random.randint(1, 9)
    var_count = 0
    print("A number between 1-9 is generated")

    while True:
        var_in = input("Guess the Number (or [e]xit to quit): ")

        if var_in.upper() in ["E", "EXIT"]:
            print("-------------------------BYE-------------------------")
            break
        var_guess = int(var_in)
        var_count += 1

        if var_guess == var_number:
            print("You Guessed the number correctly in {0} attempts".format(var_count))
            if input("Enter \"[e]xit\" to quit, or any other key to continue").upper() not in ["E", "EXIT"]:
                var_count = 0
                var_number = random.randint(1, 9)
                print("-----------------------------------------------------")
                print("A number between 1-9 is generated")
                continue
            else:
                print("-------------------------BYE-------------------------")
                break
        elif var_guess > var_number:
            if var_guess - var_number >= 5:
                print("Guessed Too High")
            else:
                print("Guessed High")
        else:
            if var_guess - var_number <= -5:
                print("Guessed Too Low")
            else:
                print("Guessed Low")
