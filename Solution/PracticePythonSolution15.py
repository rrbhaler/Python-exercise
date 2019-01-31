# Practice Python: Exercise 15
# http://www.practicepython.org/solution/2014/05/28/15-reverse-word-order-solutions.html


def solution():
    var_line = input("Enter a line: ")
    var_rev = " ".join(list(reversed(var_line.split())))

    print("Line: {0}\nReversed: {1}".format(var_line, var_rev))
