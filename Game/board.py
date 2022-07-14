import game_functions as gf


class Board():
    """ This is creating an object board with logic of checking a winner """

    def __init__(self):
        self.board =[["_", "_", "_"],
                    ["_", "_", "_"],
                    ["_", "_", "_"]]
        self.winner = 0

    def update_board(self, board):
        self.board = board

    def print_board(self):
        print("\n")
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(self.board[i][j], end=" ")
            print("\n")


    def check_win(self, board, player1, player2):

        if gf.check_win(board) == player1.counter:
            self.winner = 1
        elif gf.check_win(board) == player2.counter:
            self.winner = 2
        elif gf.check_spaces(board) == False:
            self.winner = 3

        return self.winner

    def reset_board(self):
        self.board =[["_", "_", "_"],
                     ["_", "_", "_"],
                     ["_", "_", "_"]]
        self.winner = 0
