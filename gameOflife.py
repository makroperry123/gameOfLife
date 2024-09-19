

testGrid = [[0,0,0,1],
            [1,1,1,0],
            [0,0,1,0]]

rows = len(testGrid)
cols=  len(testGrid[0])
# Each cell with one or no neighbors dies, as if by solitude.
# Each cell with four or more neighbors dies, as if by overpopulation.
# Each cell with two or three neighbors survives.
# Each cell with three neighbors becomes populated.

def gameOfLife(testGrid, gen):
    rows = len(testGrid)
    cols = len(testGrid[0])
    emptyGrid = [[None for _ in range(cols)] for _ in range(rows)]
    secondGen = [[None for _ in range(cols)] for _ in range(rows)]
    for b in range(gen):
        for i in range(rows):
            for j in range(cols):
                check = 0
                # Right (j + 1)
                if j + 1 < cols and testGrid[i][j + 1] == 1:
                    check += 1

                # Down (i + 1)
                if i + 1 < rows and testGrid[i + 1][j] == 1:
                    check += 1

                # Left (j - 1)
                if j - 1 >= 0 and testGrid[i][j - 1] == 1:
                    check += 1

                # Up (i - 1)
                if i - 1 >= 0 and testGrid[i - 1][j] == 1:
                    check += 1

                # Down-Right (i + 1, j + 1)
                if i + 1 < rows and j + 1 < cols and testGrid[i + 1][j + 1] == 1:
                    check += 1

                # Up-Right (i - 1, j + 1)
                if i - 1 >= 0 and j + 1 < cols and testGrid[i - 1][j + 1] == 1:
                    check += 1

                # Down-Left (i + 1, j - 1)
                if i + 1 < rows and j - 1 >= 0 and testGrid[i + 1][j - 1] == 1:
                    check += 1

                # Up-Left (i - 1, j - 1)
                if i - 1 >= 0 and j - 1 >= 0 and testGrid[i - 1][j - 1] == 1:
                    check += 1

                # Store the check count in emptyGrid
                emptyGrid[i][j] = check

        for i in range(rows):  # Iterate through rows first
            for j in range(cols):  # Then through columns
                # Cell becomes alive
                if testGrid[i][j] == 0 and emptyGrid[i][j] == 3:
                    secondGen[i][j] = 1
                # Cell dies from overpopulation
                elif testGrid[i][j] == 1 and emptyGrid[i][j] > 3:
                    secondGen[i][j] = 0
                # Cell dies from isolation
                elif testGrid[i][j] == 1 and emptyGrid[i][j] < 2:
                    secondGen[i][j] = 0
                # Cell survives
                elif testGrid[i][j] == 1:
                    secondGen[i][j] = 1
                else:
                    secondGen[i][j] = 0
        print(b)
        print("initial Grid")
        for p in testGrid[:]:
            print(p)

        print("#" * 33)
        print("neighbours")
        print(emptyGrid)
        print("#" * 33)
        print("next gen")
        for o in secondGen[:]:
            print(o)
        testGrid = secondGen

gameOfLife(testGrid,7)