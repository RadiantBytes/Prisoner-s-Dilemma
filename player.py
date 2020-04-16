# A simple player class to help manage functions in dilemma.py

class Player():
    # 0 if player stays silent
    # 1 if player confesses
    turn_action = -1
    last_turn_action = -1

    def __init__(self, num_points, game_strat):
        self.num_points = num_points
        self.game_strat = game_strat
        self.turn_action

    def get_points(self):
        return self.num_points

    def add_points(self, num_points):
        self.num_points += num_points

    def get_turn_action(self):
        return self.turn_action

    def get_last_turn_action(self):
        return self.last_turn_action

    def set_last_turn_action(self, game_turn):
        self.last_turn_action = game_turn

    def confess(self):
        self.turn_action = 1

    def silent(self):
        self.turn_action = 0
