from basePlayer import BasePlayer

class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Joe"
        self.icon = 'O'

    def next_move(self, board):
        self.print_board(board)
        next_move = input("What's your next move? type the square position as (row, column)")
        return next_move
