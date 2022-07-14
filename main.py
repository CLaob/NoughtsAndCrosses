from player import Player
import game_functions as gf
from noughts_and_crosses import NoughtsAndCrosses


def main():

    game = NoughtsAndCrosses()
    ask_play = input("would you like to play? (Y/N): ").lower()
    while ask_play == 'y':
        winner = game.NoughtsAndCrosses()
        gf.printWinner(winner)
        game.board.reset_board()
        ask_play = input("would you like to play? (Y/N): ").lower()


if __name__ == "__main__":
    main()
