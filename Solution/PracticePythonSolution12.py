# Practice Python: Exercise 12
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random


def list_beg_end(var_list=None):
    if var_list is None:
        var_list = []
    var_length = var_list.__len__()
    if var_length == 0:
        return []
    else:
        return [var_list[0], var_list[var_length - 1]]


def solution():
    var_list_a = []
    for _i in range(0, random.randint(1, 25)):
        var_list_a.append(random.randint(1, 99))

    var_result = list_beg_end(var_list_a)

    print(var_list_a, var_result, sep="\n")
