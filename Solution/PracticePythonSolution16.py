# Practice Python: Exercise 16
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random


def get_int(show_prompt="Enter: ", show_text=None, valid_options: list = None, invalid_options: list = None,
            min_value: int = None, max_value: int = None):
    if show_text is not None:
        print(show_text)

    while True:
        try:
            _input = int(input(show_prompt))
            if ((valid_options is not None and _input not in valid_options) or
                    (invalid_options is not None and _input in invalid_options) or
                    (min_value is not None and _input < min_value) or
                    (max_value is not None and _input > max_value)):
                pass
            else:
                return _input
        except ValueError:
            pass


def scramble_word(var_word):
    var_char_l = list(var_word)
    random.shuffle(var_char_l)
    return "".join(var_char_l)


def weak_pass():
    list_wpass = ["performance", "corresponding", "predetermined", "formatting", "tokenize", "exceptions",
                  "incremented"]
    return list_wpass[random.randint(1, list_wpass.__len__()) - 1]


def medium_pass():
    pass_len = get_int("Enter password length (min 6, max 12)", min_value=6, max_value=12)
    _password = ""
    for _i in range(0, pass_len // 3):
        _password += chr(random.randint(97, 122))  # LowerCase
        _password += chr(random.randint(65, 90))  # UpperCase
    for _i in range(0, pass_len - ((pass_len // 3) * 2)):
        _password += str(random.randint(0, 9))  # Numeric

    return scramble_word(_password)


def hard_pass():
    special_char = [33, 35, 36, 38, 42, 45, 95, 124, 126]
    pass_len = get_int("Enter password length (min 8, max 25)", min_value=8, max_value=25)
    _password = ""
    for _i in range(0, pass_len // 4):
        _password += chr(random.randint(97, 122))  # LowerCase
        _password += chr(random.randint(65, 90))  # UpperCase
        _password += str(random.randint(0, 9))  # Numeric
    for _i in range(0, pass_len - ((pass_len // 4) * 3)):
        _password += chr(special_char[random.randint(1, special_char.__len__()) - 1])  # Special Character
    return scramble_word(_password)


def gen_pass(_strength):
    return {
        0: weak_pass,
        1: medium_pass,
        2: hard_pass
    }[_strength]()


def solution():
    var_pass_strength = get_int(show_text="Password Strength:\n"
                                          "0. Weak (Dictionary Word)\n"
                                          "1. Medium (Alpha-Numeric)\n"
                                          "2. Hard (Alpha-Numeric with Special Character)\n",
                                show_prompt="Enter your choice: ",
                                valid_options=[0, 1, 2])
    print("Generated Password:      {}".format(gen_pass(var_pass_strength)))
