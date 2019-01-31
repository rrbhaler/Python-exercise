# Practice Python: Exercise 07
# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

import random


def solution():
    var_list = []
    var_limit = random.randint(10, 25)

    for _index in range(0, var_limit):
        var_list.append(random.randrange(1, 99, 1))

    var_even = list(filter(lambda x: x % 2 == 0, var_list))
    print(var_list, var_even, sep="\n")
