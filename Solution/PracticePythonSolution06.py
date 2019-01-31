# Practice Python: Exercise 06
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html


def solution():
    var_string = str(input("Enter Your String: "))
    var_reversed = var_string[::-1]

    if var_string == var_reversed:
        print(var_string, "is a Palindrome")
    else:
        print(var_string, "is NOT a Palindrome")
