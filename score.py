import collections
class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def game_over(self, win, name):
        if win:
            self.score[name] += 10