# Practice Python: Exercise 02
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html


def solution():
    var_num = int(input("Enter a Number: "))
    var_check = int(input("Enter Number to divide by: "))
    var_result = ""
    if var_num % 4 == 0:
        var_result += "{0} is a multiple of 4\n"

    if var_num % 2 == 0:
        var_result += "{0} is an Even No\n"
    else:
        var_result += "{0} is an Odd No\n"

    if var_num % var_check == 0:
        var_result += "{0} is divisible by {1}"
    else:
        var_result += "{0} is NOT divisible by {1}"

    print(var_result.format(var_num, var_check))
