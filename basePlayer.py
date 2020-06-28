from boardUtils import BoardUtils

class BasePlayer:
    def __init__(self, score_keeper):
        self.score = score_keeper

    def game_over(self, win):
        self.score.game_over(win, self.name)

    def print_board(self, board):
        utils = BoardUtils()
        utils.scan_board(
            board,
            lambda i, j, is_last: print(
                f"{board[i][j]:3}", end="\n" if is_last else ""
            ),
        )