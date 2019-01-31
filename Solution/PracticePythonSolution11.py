# Practice Python: Exercise 11
# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

import math


def check_primary(var_a):
    var_isprime = True
    for _i in range(2, int(math.ceil(math.sqrt(var_a))) + 1):
        if var_a % _i == 0:
            var_isprime = False
            break

    if var_isprime:
        print("{0} is a Prime No".format(var_a))
    else:
        print("{0} is NOT a Prime No".format(var_a))


def get_int(show_text="Enter: "):
    return int(input(show_text))


def solution():
    while True:
        var_number = get_int("Enter a Number (to Quit enter 0): ")
        if var_number == 0:
            break
        check_primary(var_number)
