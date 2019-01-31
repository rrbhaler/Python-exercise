# Practice Python: Exercise 04
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html


def solution():
    var_number = int(input("Enter a Number: "))
    var_divisors = [1]
    for var_div in range(2, (var_number // 2) + 1):
        if var_number % var_div == 0:
            var_divisors.append(var_div)
    var_divisors.append(var_number)
    print("Divisors of {0} are : {1}".format(var_number, var_divisors))
