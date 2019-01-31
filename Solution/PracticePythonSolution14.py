# Practice Python: Exercise 14
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

import random


def remove_duplicate_loop(var_list):
    var_result_list = []
    for _item in var_list:
        if _item not in var_result_list:
            var_result_list.append(_item)

    return var_result_list


def remove_duplicate_set(var_list):
    return list(set(var_list))


def check_duplicate(var_list):
    for _index in range(0, len(var_list)):
        if var_list[_index] in var_list[_index + 1:]:
            return True

    return False


def solution():
    var_initial_list = []
    for _limit in range(0, random.randint(1, 100)):
        var_initial_list.append(random.randint(1, 99))

    var_result_list_l = remove_duplicate_loop(var_initial_list)
    var_result_list_s = remove_duplicate_set(var_initial_list)

    print(
        "{0}\n{1}\n{2}\n{3}".format(var_initial_list, var_result_list_l, var_result_list_s, sorted(var_result_list_l)))
    print("Final List Doesn't contains duplicate: {0}".format(not check_duplicate(var_result_list_l)))
    print("Final List Doesn't contains duplicate: {0}".format(not check_duplicate(var_result_list_s)))
