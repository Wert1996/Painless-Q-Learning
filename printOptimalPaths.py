import numpy as np
from calculateQ import calQ


def calculateAllPaths():
    Q = calQ()
    paths = []
    maxInd = np.argmax(Q, axis = 1)
    for i in range(6):
        curPath = []
        curPath.append(str(i))
        current = i
        while(current != 5):
            current = maxInd[current]
            curPath.append(str(current))
        paths.append("->".join(curPath))
    return paths


if __name__ == "__main__":
    paths = calculateAllPaths()
    initial = int(input("Input the starting point: "))
    try:
        print(paths[initial])
    except:
        print("Enter a valid number between 0-5 bruh..")

