# Practice Python: Exercise 05
# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random


def solution():
    var_list_a = []
    var_list_b = []

    var_limit = random.randint(10, 20)
    for _r in range(1, var_limit):
        var_list_a.append(random.randrange(50, 59, 1))

    var_limit = random.randint(10, 20)
    for _r in range(1, var_limit):
        var_list_b.append(random.randrange(50, 59, 1))

    var_list_common = list(set(filter(lambda x: x in var_list_b, var_list_a)))

    print(sorted(var_list_a), sorted(var_list_b), sorted(var_list_common), sep="\n")
