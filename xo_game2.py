import collections
from score import Score
from boardUtils import BoardUtils
from basePlayer import BasePlayer
from humanPlayer import HumanPlayer
from aiPlayer import AIPlayer

def updateBoard(iboard, point, icon):
    global board
    x = int(point.split(',')[0])
    y = int(point.split(',')[1])
    if board[x][y] == '.':
        board[x][y] = icon
    else:
        print("this cell is taken, nothing happened")

print("hello")
board_utils = BoardUtils()
score_keeper = Score()
h = HumanPlayer(score_keeper)
a = AIPlayer(score_keeper)
players = [h, a]
current_player = 0
board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

while not board_utils.game_over(board):
    print(f"now is the turn of {players[current_player].name}")
    print("this is the board before the move")
    point = players[current_player].next_move(board)
    updateBoard(board, point, players[current_player].icon)
    current_player = (current_player + 1) % len(players)
    #     print(current_player)
    #     point = players[current_player].next_move(board)
    #     print(point)
    #     board_utils.updateBoard(board, point, players[current_player])
    # players[current_player].game_over(True)
    #
    # # h.next_move(board)
    # #
    # # res = a.next_move(board)
    # # print(res)
    #
    # a.game_over(True)
    # a.game_over(True)
    # h.game_over(True)
    #
    # print(h.score.score)