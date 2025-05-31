# EightPuzzleAgent: A goal-based agent that emits the actions from a solution to
# an "eight puzzle" problem.
# Your implementation should pass the tests in test_eight_puzzle_agent.py.
# Cindy Chen

from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_transition_model import EightPuzzleTransitionException


class EightPuzzleAgent:
    def __init__(self, initial_state,transition_model=None,actions=None):
        """ Initialize the agent. """
        self.current_state = initial_state
        self.transition_model = transition_model if transition_model else EightPuzzleTransitionModel()
        self.actions = actions
    

    def has_actions(self):
        """ Return `True` when `self.actions` is not empty. """
        return len(self.actions) > 0

    def action(self):
        """Returns the next valid callable action from `self.actions`."""
        if  self.has_actions():
            next_action = self.actions.pop(0)
            return next_action
        return None 

    def move_left(self):
        try:
            self.current_state = self.transition_model.move_left(self.current_state)
            print("Move Left")
        except EightPuzzleTransitionException as e:
            print(f"Cannot move left: {e}")

    def move_right(self):
        try:
            self.current_state = self.transition_model.move_right(self.current_state)
            print("Move Right")
        except EightPuzzleTransitionException as e:
            print(f"Cannot move right: {e}")

    def move_up(self):
        try:
            self.current_state = self.transition_model.move_up(self.current_state)
            print("Move Up")
        except EightPuzzleTransitionException as e:
            print(f"Cannot move up: {e}")

    def move_down(self):
        try: 
            self.current_state = self.transition_model.move_down(self.current_state)
            print("Move Down")
        except EightPuzzleTransitionException as e:
            print(f"Cannot move down: {e}")
