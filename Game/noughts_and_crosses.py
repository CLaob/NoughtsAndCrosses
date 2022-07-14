from player import Player
from board import Board
import game_functions as gf


class NoughtsAndCrosses:

    def __init__(self):
        self.board = Board()
        self.player1 = Player(1)
        self.player2 = Player(2)

    def NoughtsAndCrosses(self):
        gf.set_counters(self.player1, self.player2)
        gf.set_turn(self.player1, self.player2)
        gf.intro(self.player1, self.player2, self.board)

        while self.board.winner == 0:

            if self.player1.turn:
                update_move = self.player1.place_move(self.board)
                self.player2.turn = True
            else:
                update_move = self.player2.place_move(self.board)
                self.player1.turn = True

            self.board.update_board(update_move)
            self.board.print_board()

            self.board.check_win(self.board.board,self.player1, self.player2)

        return self.board.winner
