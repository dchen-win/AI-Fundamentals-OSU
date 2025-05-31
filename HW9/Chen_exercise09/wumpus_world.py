# WumpusWorld
# A simulated representation of a real Wumpus World, aligned with the specified
# characteristics in the AIMA text.
# Note: This is not a state model. It _is_ the real world / environment within
# which the agent operates. Think of it as actual, physical, reality.
# Note 2: This simulation will not include the modeling of time, for the sake of
# simplicity. This only affects the 'Bump' and 'Scream' percepts. In the case of
# 'Bump', we assume that when an agent is in a room facing a wall, it should receive
# the 'Bump' percept. For 'Scream', when the wumpus is killed we let the scream
# linger throughout the cave indefinitely.


from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

class WumpusWorld:

    EXIT_LOCATION = (1, 1)

    def __init__(self, agent_location=(1, 1), agent_direction="East",
             agent_alive=True, wumpus_alive=None, wumpus_location=None,
             gold_location=None, pit_locations=[], world_size=(4, 4)):
        self.agent_location = agent_location
        self.agent_direction = agent_direction
        self.agent_alive = agent_alive
        self.wumpus_alive = wumpus_alive
        self.wumpus_location = wumpus_location
        self.gold_location = gold_location
        self.pit_locations = pit_locations
        self.scream = not self.wumpus_alive 
        self.world_size = world_size

    def percept(self, location):
        if location is None:
            return (None, None, None, None, None)
        stench = breeze = glitter = bump = scream = None
        if location == self.wumpus_location or self.adjacent(location, self.wumpus_location):
            stench = 'Stench'

        if any(self.adjacent(location, pit) for pit in self.pit_locations):
            breeze = 'Breeze'

        if location == self.gold_location:
            glitter = 'Glitter'

        if self.agent_bumped_wall():
            bump = 'Bump'
        
        if not self.wumpus_alive:
            scream = 'Scream'

        return (stench, breeze, glitter, bump, scream)


    def turned_left(self):
        directions = ['North', 'West', 'South', 'East']
        current_idx = directions.index(self.agent_direction)
        self.agent_direction = directions[(current_idx + 1) % 4]

    def turned_right(self):
        directions = ['North', 'East', 'South', 'West']
        current_idx = directions.index(self.agent_direction)
        self.agent_direction = directions[(current_idx + 1) % 4]


    def moved_forward(self):
        if self.agent_direction == "North":
            new_location = (self.agent_location[0], self.agent_location[1] + 1)
        elif self.agent_direction == "South":
            new_location = (self.agent_location[0], self.agent_location[1] - 1)
        elif self.agent_direction == "West":
            new_location = (self.agent_location[0] - 1, self.agent_location[1])
        elif self.agent_direction == "East":
            new_location = (self.agent_location[0] + 1, self.agent_location[1])
        else:
            return 

        if not (1 <= new_location[0] <= 4 and 1 <= new_location[1] <= 4):
            return

        self.agent_location = new_location

        if new_location in self.pit_locations:
            self.agent_alive = False
            return 

        if new_location == self.wumpus_location and self.wumpus_alive:
            self.agent_alive = False
            return 

    def grabbed(self):
        if self.agent_location == self.gold_location:
            self.gold_location = None

    def climbed(self):
        if self.agent_location == self.EXIT_LOCATION:
            self.agent_location = None

    def shot(self):
        if self.agent_alive and self.wumpus_alive:

            if self.agent_direction == "East" and self.agent_location[1] == self.wumpus_location[1] and self.agent_location[0] < self.wumpus_location[0]:
                self.wumpus_alive = False
                

            elif self.agent_direction == "West" and self.agent_location[1] == self.wumpus_location[1] and self.agent_location[0] > self.wumpus_location[0]:
                self.wumpus_alive = False
    

            elif self.agent_direction == "North" and self.agent_location[0] == self.wumpus_location[0] and self.agent_location[1] < self.wumpus_location[1]:
                self.wumpus_alive = False
    

            elif self.agent_direction == "South" and self.agent_location[0] == self.wumpus_location[0] and self.agent_location[1] > self.wumpus_location[1]:
                self.wumpus_alive = False


    """
    Helper methods
    """

    def adjacent(self, location, target):
        if location is None or target is None:
            return False
        
        return (abs(location[0] - target[0]) == 1 and location[1] == target[1]) or \
            (abs(location[1] - target[1]) == 1 and location[0] == target[0])

    def agent_can_move_east(self):
 
       return self.agent_location[0] < 4

    def agent_can_move_west(self):

        return self.agent_location[0] > 1


    def agent_can_move_north(self):

        return self.agent_location[1] < 4

    
    def agent_can_move_south(self):

        
        return self.agent_location[1] > 1


    def agent_bumped_wall(self):
        col, row = self.agent_location
        if self.agent_direction == 'West' and col == 1:
            return True

        elif self.agent_direction == 'South' and row == 1:
            return True

        elif self.agent_direction == 'East' and col == 4:
            return True

        elif self.agent_direction == 'North' and row == 4:
            return True
        return False


    def wumpus_east_of_agent(self):

        same_column = self.wumpus_location[1] == self.agent_location[1]
        east_of_agent = self.wumpus_location[0] > self.agent_location[0]
        return east_of_agent
    
    def wumpus_west_of_agent(self):

        same_column = self.wumpus_location[1] == self.agent_location[1]  
        west_of_agent = same_column and self.wumpus_location[0] < self.agent_location[0] 
        return west_of_agent

    def wumpus_north_of_agent(self):

        same_row = self.wumpus_location[0] == self.agent_location[0]  
        north_of_agent = same_row and self.wumpus_location[1] > self.agent_location[1]  
        return north_of_agent


    def wumpus_south_of_agent(self):

        same_row = self.wumpus_location[0] == self.agent_location[0]  
        south_of_agent = same_row and self.wumpus_location[1] < self.agent_location[1]  
        return south_of_agent
