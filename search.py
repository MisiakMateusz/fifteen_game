from game import *
from State import State


class BFS:
    def __init__(self, start):
        self.game = Game(start)
        self.visited = {}
        self.explored = set()

    def search(self):
        # # First state

        if self.game.check_result(self.game):
            print('You win at first iteration!')
            return ''

        for move in self.game.available_moves(self.game):
            new_state = self.game.swap(self.game, move)
            print(new_state)

            # Check if this goal state
            if self.game.check_result(new_state):
                for key, value in self.visited.items():
                    print('%s : \n%s\n' % (key, value))
                return
            else:
                self.visited[new_state.frame.tostring()] = new_state
            # if self.game.check_result(new_state):
            #     break




