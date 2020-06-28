class BoardUtils:
    def scan_board(self, board, code_to_run_for_each_item):
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board[i]) - 1)
                if res is not None:
                    return res

    def game_over(self, board):
        return False