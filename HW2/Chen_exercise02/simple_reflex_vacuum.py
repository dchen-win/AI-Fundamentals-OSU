# SimpleReflexVacuum: A robot vacuum cleaner modeled as a simple reflex agent.
# Your implementation should pass the tests in test_simple_reflex_vacuum.py.
# Cindy Chen


class SimpleReflexVacuum:

    def __init__(self):
        '''Initializes the SimpleReflexVacuum class.'''
        pass
    
    # Actuators
    def suck(self):
        '''Simulates the vacuum sucking up dirt at its current location.'''
        print("SUCK")

    def move_left(self):
        '''Simulates the vacuum moving to the left.'''
        print("MOVE LEFT")

    def move_right(self):
        '''Simulates the vacuum moving to the right.'''
        print("MOVE RIGHT")

    def action(self, location, dirt_status):
        '''Determines the next action based on the current location and dirt status.'''
        if dirt_status:
            return self.suck
        elif location == "A":
            return self.move_right
        elif location == "B":
            return self.move_left
