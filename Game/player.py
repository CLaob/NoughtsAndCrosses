import game_functions as gf


class Player:
    """ Creating the Player Class for Player 1 and Player 2 """

    def __init__(self, player_num):
        self.playerNum = player_num
        self.counter = ""
        self.turn = False
        self.win = False

    def define_counter(self):
        self.counter = "X" if self.playerNum == 1 else "O"

    def place_move(self, board):
        update_board = board.board

        try:
            move_x = int(input(gf.input_message(self.playerNum, "row")))-1
            move_y = int(input(gf.input_message(self.playerNum, "column")))-1

            while gf.is_valid_move(move_x, move_y, update_board):
                print("INVALID INPUT: ")
                move_x = int(input(gf.input_message(self.playerNum, "row")))-1
                move_y = int(input(gf.input_message(self.playerNum, "column")))-1

            update_board[move_x][move_y] = self.counter

        except:
            print("INVALID INPUT: ")

        self.turn = False

        return update_board
