import collections

class BoardUtils:
    def scan_board(self, board, code_to_run_for_each_item):
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board[i]) - 1)
                if res is not None:
                    return res

    def _is_all_the_same(self, board, i1, i2, i3, val):
        if (board[i1[0]][i1[1]] == board[i2[0]][i2[1]] and
                board[i1[0]][i1[1]] == board[i3[0]][i3[1]] and
                board[i1[0]][i1[1]] == val):
            return True
        else:
            return False

    def get_winner(self, board):
        for player in ['X', 'O']:
            # rows
            if self._is_all_the_same(board, (0, 0), (0, 1), (0, 2), player): return player
            if self._is_all_the_same(board, (1, 0), (1, 1), (1, 2), player): return player
            if self._is_all_the_same(board, (2, 0), (2, 1), (2, 2), player): return player

            # columns
            if self._is_all_the_same(board, (0, 0), (1, 0), (2, 0), player): return player
            if self._is_all_the_same(board, (0, 1), (1, 1), (2, 1), player): return player
            if self._is_all_the_same(board, (0, 2), (1, 2), (2, 2), player): return player

            # diagonals
            if self._is_all_the_same(board, (0, 0), (1, 1), (2, 2), player): return player
            if self._is_all_the_same(board, (0, 2), (1, 1), (2, 0), player): return player

    def game_over(self, board):
        if self.get_winner(board) == None:
            return False
        else:
            return False

    def updateBoard(self, board, point, player):
        x = int(point.split(',')[0])
        y = int(point.split(',')[1])
        try:
            board[x][y] = player.icon
        except IndexError:
            print("Out of range")


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)


    def game_over(self, win, name):
        if win:
            self.score[name] += 10


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



class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        print(self.score)
        self.name = "Joe"
        self.icon = 'O'

    def next_move(self, board):
        self.print_board(board)
        next_move = input("What's your next move? type the square position as (row, column)")
        return next_move

class AIPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Bot"
        self.icon= 'X'

    def next_move(self, board):
        def foreach_cell(i, j, is_last):
            if board[i][j] == '.':
                print(board[i][j])
                return f"{j}, {i}"

        utils = BoardUtils()
        return utils.scan_board(
            board,
            foreach_cell,
        )


if __name__ == '__main__':
    board_utils = BoardUtils()
    score_keeper = Score()
    h = HumanPlayer(score_keeper)
    a = AIPlayer(score_keeper)
    board = [['X', '.', '.'], ['O', '.', '.'], ['.', '.', '.']]
    players = [h, a]
    current_player = 0
    while not board_utils.game_over(board):
        players[current_player].print_board(board)
        current_player = (current_player + 1) % len(players)
        print(current_player)
        point = players[current_player].next_move(board)
        print(point)
        board_utils.updateBoard(board, point, players[current_player])
    players[current_player].game_over(True)

    # h.next_move(board)
    #
    # res = a.next_move(board)
    # print(res)

    a.game_over(True)
    a.game_over(True)
    h.game_over(True)

    print(h.score.score)