# Practice Python: Exercise 03
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

import random


def solution():
    var_list = []
    for r in range(0, 20):
        var_list.append(random.randrange(1, 50, 1))
    var_threshold = int(input("Enter Threshold Number: "))
    print("SubList: ", list(filter(lambda x: x < var_threshold, var_list)))
    print(sorted(var_list), var_threshold, sep="\n")
