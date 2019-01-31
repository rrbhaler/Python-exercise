# Practice Python: Exercise 18
# http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random


def get_int(show_prompt="Enter: ", show_text=None, valid_options: list = None, invalid_options: list = None,
            min_value: int = None, max_value: int = None):
    if show_text is not None:
        print(show_text)

    while True:
        try:
            _input = int(input(show_prompt))
            if ((valid_options is not None and _input not in valid_options) or
                    (invalid_options is not None and _input in invalid_options) or
                    (min_value is not None and _input < min_value) or
                    (max_value is not None and _input > max_value)):
                pass
            else:
                return _input
        except ValueError:
            pass


def calculate_cow_bull(_number, _guess):
    cow = bull = 0
    _number = str(_number)
    _temp = _number
    _guess = str(_guess)
    for _i in range(0, 4):
        if _guess[_i] in _number:
            if _guess[_i] == _temp[_i]:
                cow += 1
            else:
                bull += 1

            _loc = _number.find(_guess[_i])
            _number = _number[:_loc] + _number[_loc + 1:]

    return [cow, bull]


def solution():
    print("*********************   COWS   AND   BULLS   *********************\n"
          "*                                                                *\n"
          "*    Guess a 4-digit number. For every digit guessed correctly   *\n"
          "*    in the correct place, you have a “cow”. For every digit     *\n"
          "*    guessed correctly in the wrong place is a “bull.”           *\n"
          "*    After every guess you will be notified how many “cows”      *\n"
          "*    and “bulls” you have.                                       *\n"
          "*    Once you guesses the correct number, the game is over.      *\n"
          "*                                                                *\n"
          "******************************************************************\n")
    var_number = random.randint(1000, 9999)
    var_count = 0
    print(var_number)
    while True:
        var_guess = get_int("Enter a 4 digit number: ", min_value=1000, max_value=9999)
        var_count += 1
        if var_guess == var_number:
            print("\n\n"
                  "                                    "
                  "You guessed the number {0} correctly in {1} attempts.\n".format(var_number, var_count))
            break
        else:
            cow_bull = calculate_cow_bull(var_number, var_guess)
            print("                                     "
                  "Number {0} has {1} Cows and {2} Bulls".format(var_guess, cow_bull[0], cow_bull[1]))
