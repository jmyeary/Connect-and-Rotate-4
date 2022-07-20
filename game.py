#https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf

import numpy as np
from functions import *
from variables import *

board = create_board()

def main():
    print(board)
    print('To play: enter an integer between 1 to 7 ' + \
          'corresponding to each column in the board. ' + \
          'You may also choose the rotation move, which' + \
          'rotates the board and drops all pieces to the' + \
          'bottom of the board, maintaining their columns.' +\
          'Whoever stacks 4 pieces next to each other, ' + \
          'either horizontally, vertically or diagonally wins.')

    game = False

    while not game:

        # Player 1
        if TURN == 0:
            user_choice = str(input("Pick a column 1-7, or enter R for Rotation"))
            if 1 <= int(user_choice) and int(user_choice) <= HEIGHT:
                choice = int(user_choice)-1
                placement(choice, board)
            elif user_choice == "R":
                rotate(board)
            else:
                raise "Invalid selection! Try again"
            game = win_conditions(board)
            next_turn(TURN)

        # Player 2
        if TURN == 1:
            string_user_choice = str(input("Pick a column 1-7, or enter R for Rotation"))
            num_user_choice = int(string_user_choice)
            if 1 <= num_user_choice and num_user_choice <= HEIGHT:
                choice = int(num_user_choice)-1
                placement(choice, board)
            elif string_user_choice == "R":
                rotate(board)
            else:
                raise "Invalid selection! Try again"
            game = win_conditions(board)
            next_turn(TURN)
    print(f'Good game! Player {TURN+1} wins!')

if __name__ == '__main__':
    main()