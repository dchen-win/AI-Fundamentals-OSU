from transition_model import TransitionModel
from state import State
class ModelReflexVacuum:

    def __init__(self, state, transition_model, sensor_model):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None

    # Sensors
    def sense_location_id(self):
        """Returns the current location ID ('A' or 'B')."""
        return self.sensor_model.sense_location_id()

    def sense_dirt(self):
        """Returns True if dirt is detected in the current location, False otherwise."""
        return self.sensor_model.sense_dirt()

    # Actuators
    def suck(self):
        """Applies suction to clean the current location."""
        self.transition_model.apply_suction()
       

    def move_left(self):
        """Moves the vacuum to the left."""
        self.transition_model.move_left()
      

    def move_right(self):
        """Moves the vacuum to the right."""
        self.transition_model.move_right()


    def update_state(self):
        if self.most_recent_action:
            self.most_recent_action()
            
    # Agent function
    def action(self):
        """Determines and executes the next action for the vacuum cleaner."""
        if self.sense_dirt():
            self.most_recent_action = self.suck
            self.update_state()
        elif self.sense_location_id() == 'A':
            self.most_recent_action = self.move_right
            self.update_state()
        elif self.sense_location_id() == 'B':
            self.most_recent_action = self.move_left
            self.update_state()
        else:
            self.most_recent_action = None
        
        return self.most_recent_action