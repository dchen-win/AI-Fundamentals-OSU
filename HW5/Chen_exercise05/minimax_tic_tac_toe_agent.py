# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Cindy Chen

from tic_tac_toe_game import TicTacToeGame
import math

class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        if game is None:
            self.game = TicTacToeGame([None] * 9, None)
        else:
            self.game = game
        self.symbol = symbol 

    def action(self, state):
        """
        Returns the best action for the agent to take from the current state.

        :param state: The current game state.
        :return: The best action (move) that the agent should take.
        """
        return self.minimax(self.game, state)
    
    def minimax(self, game, state):
        """
        Minimax search function to select the best move.

        This function implements the recursive minimax algorithm, which evaluates
        the game tree by calling the `max_value` and `min_value` functions based on
        whose turn it is.
        """

        player = game.to_move(state)
    
        value, move = self.max_value(game, state)
    
        return value, move
    def max_value(self, game, state):
        """
        Compute the maximum value for the current state (maximizing player's turn).
        """
        if game.is_terminal(state):
            return game.utility(state, self.symbol), None
        
        value = -math.inf
        move = None
        for action in game.actions(state):
            new_state = game.result(state, action)
            new_value, _ = self.min_value(game, new_state)
            if new_value > value:
                value, move = new_value, action
        return value, move

    def min_value(self, game, state):
        """
        Compute the minimum value for the current state (minimizing player's turn).
        """
        if game.is_terminal(state):
            return game.utility(state, self.symbol), None
        
        value = math.inf
        move = None

        for action in game.actions(state):
            new_state = game.result(state, action)
            new_value, _ = self.max_value(game, new_state)
            if new_value < value:
                value, move = new_value, action
        return value, move
