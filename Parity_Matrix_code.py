import numpy as np  # we import numpy library
import time # we import time library so we can see how fast is our code later

rows = 0
col = 0

def get_input():
    global rows
    global col

    given_matrix = []

    rows, col = input().split()
    rows = int(rows)
    col = int(col)

    for row in range(rows):
        new_row = input().split()
        new_row = [int(i) % 2 for i in new_row]
        given_matrix.append(new_row)

    return given_matrix


def conditions_check(matrix):
    global rows
    global col

    nmatrix = np.array(matrix) # we transform the matrix into numpy array, so we can easier index the columns and rows

    parity = [["."]*col for i in range(rows)]
    # print(*(' '.join(row) for row in parity), sep='\n')

    for r in range(rows):
        for c in range(col):
            # print("Analizing element in position", r,c, " - ", matrix[r][c])
            if c >= 2:
                if nmatrix[r,c-1] == nmatrix[r][c-2]:
                    parity[r][c] = "X"
                else:
                    break
        for c in range(col-1,-1,-1):
            if c <= col-3:
                if nmatrix[r, c+1] == nmatrix[r, c+2]:
                    parity[r][c] = "X"
                else:
                    break

    for c in range(col):
        for r in range(rows):
            if r >= 2:
                if nmatrix[r-1, c] == nmatrix[r-2, c]:
                    parity[r][c] = "X"
                else:
                    break

        for r in range(rows-1,-1,-1):
            if r <= rows-3:
                if nmatrix[r+1, c] == nmatrix[r+2, c]:
                    parity[r][c] = "X"
                else:
                    break

    print(*(' '.join(row) for row in parity), sep='\n')



# start = time.time()  # this is the start of time

# we call the functions
given_matrix = get_input()
conditions_check(given_matrix)

# finish = time.time() # this is the finish time and we print (finish-start) time in seconds
# print("--- %s seconds ---" % (finish-start))