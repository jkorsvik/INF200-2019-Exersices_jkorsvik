# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"


class Board:
    """
    Handles the information about the board, including ladders, snakes,
    goal.

    Methods:
        constructor

        goal_reached

        position_adjustment
    """
    def __init__(self, ladders=None, chutes=None, goal=None):
        if ladders is not None:
            self.ladders = ladders
        else:
            self.ladders = [(1, 40), (8, 10), (36, 52), (43, 62),
                            (49, 79), (65, 82), (68, 85)]
        if chutes is not None:
            self.chutes = chutes
        else:
            self.chutes = [(24, 5), (33, 3), (42, 30), (56, 37),
                           (64, 27), (74, 12), (87, 70)]
        if goal is not None:
            self.goal = goal
        else:
            self.goal = 90

    def goal_reached(self, position):
        return position >= self.goal

    def position_adjustment(self, position):
        for ladder in self.ladders:
            if position == ladder[0]:
                return ladder[1] - ladder[0]
        for chute in self.chutes:
            if position == chute[0]:
                return chute[1] - chute[0]
        return 0

class Player:
    """
    __init___
    input - instance of Board

    Methods:
        move() - Moves player and checks with board position

    """
    def __init__(self):
        pass

class LazyPlayer(Player):
    """
    Subclass of player
    """

    def __init__(self):
        super().__init__()


class ResilientPlayer(Player):
    """
    Subclass of player
    """
    def __init__(self):
        super().__init__()


class Simulation:
    """
    Manages simulation of the
    """

    def singe_game(self):
        pass

    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass



