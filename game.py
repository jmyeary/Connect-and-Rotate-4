#https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf

import numpy as np
from functions import *
from variables import *

create_board()

def main():
    print(board + \)
    print('To play: enter an integer between 1 to 7 ' + \
          'corresponding to each column in the board. ' + \
          'You may also choose the rotation move, which' + \
          'rotates the board and drops all pieces to the' + \
          'bottom of the board, maintaining their columns.' +\
          'Whoever stacks 4 pieces next to each other, ' + \
          'either horizontally, vertically or diagonally wins.')

    game = False

    while game == False:

        # Player 1
        if turn == 0:
            board, Stacks = move('X',board,Stacks,computer1)
            printBoard(board)
            game = win_conditions(board)
            if game == True:
                break

        # Player 2
        if turn == 1:
            board, Stacks = move('O',board,Stacks,computer1)
            printBoard(board)
            game = win_conditions(board)
            if game == True:
                break
    print('Good game.')