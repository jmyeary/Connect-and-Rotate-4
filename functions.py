import numpy as np
from variables import *


def create_board():
    board = np.zeros((HEIGHT, LENGTH), dtype=int)
    return board


def next_turn(n=TURN):
    n += 1
    n = n % 2
    return n


def placement(col, state):
    for i in range(LENGTH):
        if np.flip(state[:, col])[i] != 0:
            continue
        else:
            np.flip(state[:, col])[i] = 1
            break
    print(state)
    return state


def rotate(state):
    rotation = np.rot90(state)
    for i in range(LENGTH):
        count = sum(rotation[:, i])
        rotation[:, i] = np.zeros(LENGTH)
        position = LENGTH - 1
        while count > 0:
            rotation[:, i][position] = 1
            position -= 1
            count -= 1
    state = rotation
    print(state)
    return state


def win_conditions(state):
    rows = np.nonzero(state)[0]
    cols = np.nonzero(state)[1]
    coordinates = list(zip(rows, cols))



    # Vertical win check
    for i in range(LENGTH):
        vertical = np.diff(state[:, i])
        if np.count_nonzero(vertical == 0) >= 3:
            return True
        else:
            continue

    # Horizontal win check
    for i in range(HEIGHT):
        horizontal = np.diff(state[i, :])
        if np.count_nonzero(horizontal==0) >= 3:
            return True
        else:
            continue

    # diagonal win check
    for a in coordinates:
        # Descending diag check
        if (a[0] + 1 and a[0] + 2 and a[0] + 3) in rows and (a[1] + 1 and a[1] + 2 and a[1] + 3) in cols:
            return True
        # Ascending diag check
        elif (a[0] + 1 and a[0] + 2 and a[0] + 3) in rows and (a[1] - 1 and a[1] - 2 and a[1] - 3) in cols:
            return True
        else:
            continue
