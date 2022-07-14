import random
import numpy as np


def is_valid_move(move_x, move_y, update_board):
    return (move_x < 0 or move_x > 3) or (move_y < 0 or move_y > 3) or (update_board[move_x][move_y] != "_")


def check_win_count(win_count):
    if win_count == 3:
        return True
    else:
        return False


def input_message(player,row_col):
    message_input = f"Player {player} Please enter a {row_col} number: "
    return message_input


def set_counters(player1,player2):
    player1.define_counter()
    player2.define_counter()


def set_turn(player1,player2):
    start = random.randint(1, 10)
    if start > 5:
        player1.turn = True
    else:
        player2.turn = True


def intro(player1, player2, board):
    print("Press Space to start game")
    print("PLAYER 1 COUNTER: ", player1.counter)
    print("PLAYER 2 COUNTER: ", player2.counter)
    print("Starting Board: \n")
    board.print_board()
    print()


def check_rows_col(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0


def check_spaces(board):

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "_":
                return True

    return False


def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]

    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0


def check_win(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = check_rows_col(newBoard)
        # If winner in rows or col found the return
        if result:
            return result

    return check_diagonals(board)


def printWinner(winner):
    if winner == 1:
        print("PLAYER 1 WINS !!")
    elif winner == 2:
        print("PLAYER 2 WINS !!")
    elif winner == 3:
        print("A DRAW!")