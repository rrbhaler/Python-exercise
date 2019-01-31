# Practice Python: Exercise 10
# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random


def solution():
    var_list_a = []
    var_list_b = []

    var_limit = random.randint(10, 20)
    for _r in range(1, var_limit):
        var_list_a.append(random.randrange(1, 49, 1))

    var_limit = random.randint(10, 20)
    for _r in range(1, var_limit):
        var_list_b.append(random.randrange(1, 49, 1))

    var_common = list(set([a for a in var_list_a if a in var_list_b]))

    print(sorted(var_list_a), sorted(var_list_b), sorted(var_common), sep="\n")
