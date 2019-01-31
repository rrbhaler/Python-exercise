# Practice Python: Exercise 08
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


def solution():
    name_player1 = input("[Player 1]: Enter Name: ")
    name_player2 = input("[Player 2]: Enter Name: ")

    while True:
        # var_player1 = var_player2 = ""
        var_options = {'ROCK': 1, 'R': 1, 'PAPER': 2, 'P': 2, 'SCISSORS': 3, 'S': 3}

        while True:
            var_player1 = input("[Player 1 | {0}]: Enter [R]ock / [P]aper / [S]cissors: ".format(name_player1))
            var_player2 = input("[Player 2 | {0}]: Enter [R]ock / [P]aper / [S]cissors: ".format(name_player2))

            if var_player1.upper() not in var_options.keys() or var_player2.upper() not in var_options.keys():
                print("Please enter valid choice from :"
                      "R/Rocks"
                      "P/Paper"
                      "S/Scissors")
                continue
            else:
                break

        var_result = var_options.get(var_player1) - var_options.get(var_player2)

        if var_result == 0:
            print("Match TIE")
        elif var_result in [1, -2]:
            print("WINNER: {0}".format(name_player1))
        else:
            print("WINNER: {0}".format(name_player2))

        var_exit = input("Enter any key to continue or [Q]uit: ")
        if var_exit.upper() in ["Q", "QU", "QUI", "QUIT"]:
            break
