import os
import time
print("start")
def proofTest(matrix, solution):
    def clear():
        os.system("cls")
        return

    x = input("Visual proof? y/n")
    if x == "n":
        return
    for step in solution:
        clear()
        toScreen = []
        for x in range(len(matrix)):
            out = ''
            for y in range(len(matrix[0])):
                if (x, y) == step:
                    out += "X "
                elif matrix[x][y] == 0:
                    out += "= "
                else:
                    out += ". "
            toScreen.append(out)
        for line in toScreen:
            print(line)
        time.sleep(.05)
    print(str(len(solution)) + " steps.")
    return
