# Practice Python: Exercise 01
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime


def solution():
    var_year = datetime.datetime.now().year
    var_name = input("Enter Your Name: ")
    var_age = int(input("Enter Your Current Age: "))
    var_repeat = int(input("Repeat Count: "))

    for r in range(0, var_repeat):
        print("Hello {0}, You will be turning 100 in the Year {1}".format(var_name, var_year + (100 - var_age)))
