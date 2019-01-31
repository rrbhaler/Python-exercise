# Practice Python: Exercise 13
# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def find_fibonacci(var_term):
    var_fib_list = [1, 1]

    if var_term <= 2:
        return var_fib_list[0:var_term]

    var_len = 2
    while var_term > 2:
        var_fib_list.append(var_fib_list[var_len - 2] + var_fib_list[var_len - 1])
        var_len += 1
        var_term -= 1

    return var_fib_list


def get_int(show_text="Enter: "):
    while True:
        try:
            return int(input(show_text))
        except ValueError:
            pass


def solution():
    var_term = get_int("Enter term: ")
    print("{0} elements in Fibonacci Series are : {1}".format(var_term, find_fibonacci(var_term)))
