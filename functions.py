import numpy as np
from variables import *

def create_board():
	board = np.zeros((HEIGHT, LENGTH), dtype=int)
	return board

def whose_turn(n=TURN):
    n += 1
    n = n%2
    return n


def placement(col, state=board):
    for i in range(LENGTH):
        if np.flip(state[:, col])[i] != 0:
            continue
        else:
            np.flip(state[:, col])[i] = 1
            break
    whose_turn(TURN)
    return state


def rotate(state=board):
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
    whose_turn(TURN)
    return state


def win_conditions(state=board):
    game = False
    rows = np.nonzero(state)[0]
    cols = np.nonzero(state)[1]
    coordinates = list(zip(rows, cols))

    # Vertical win check
    for i in range(LENGTH):
        if sum(state[:, i]) >= 4:
            return True
        else:
            continue

    # Horizontal win check
    for i in range(HEIGHT):
        if sum(state[i, :]) >= 4:
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
