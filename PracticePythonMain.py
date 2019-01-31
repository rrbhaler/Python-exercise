import time

from PracticePythonExcercise import Util

if __name__ == "__main__":
    ts_clock = time.clock()
    print("START")

    while True:
        var_problem = Util.get_integer("Enter the Problem No", "Quit", "Help")
        if var_problem is None:
            print("End")
            break
        else:
            Util.call_solution(var_problem)

    te_clock = time.clock()
    print("\n\n------------------------------------------------------------------------------------------------\n",
          "Total RunTime: {} Sec".format(te_clock - ts_clock),
          "\n------------------------------------------------------------------------------------------------\nFINISH",
          sep=" || ")
