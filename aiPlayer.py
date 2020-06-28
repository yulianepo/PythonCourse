from basePlayer import BasePlayer
from boardUtils import BoardUtils

class AIPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Bot"
        self.icon= 'X'

    def next_move(self, board):
        self.print_board(board)
        def foreach_cell(i, j, is_last):
            if board[i][j] == '.':
                print(board[i][j])
                return f"{j}, {i}"

        utils = BoardUtils()
        return utils.scan_board(
            board,
            foreach_cell,
        )
