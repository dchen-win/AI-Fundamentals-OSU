# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.
# Cindy Chen

class WumpusWorldAgent:

    def __init__(self, kb):

        self.kb = kb  
        self.time = 0 
    
    def make_action_query(self):
        print("Creating an action query to ask the knowledge base.")
        return "What should I do next?"
    
    def turn_left(self, world):
        print("Turning left")
        world.turned_left()

    def turn_right(self, world):
        print("Turning right")
        world.turned_right()

    def move_forward(self, world):
        print("Moving forward")
        world.moved_forward()

    def grab(self, world):
        print("Grabbing object")
        world.grabbed()

    def shoot(self, world):
        print("Shooting the arrow")
        world.shot()

    def climb(self, world):
        print("Climbing out")
        world.climbed()
    
    def make_percept_sentence(self, percepts):
        print(f"Creating percept sentence based on percepts: {percepts}")
        percept_sentence = f"Percept: {percepts}"
        return percept_sentence

    def action(self, percept, world=None):
        self.kb.tell(percept)
        action = self.kb.ask(None)
        if world:
            if action == 'turn_left':
                return self.turn_left
            elif action == 'turn_right':
                return self.turn_right
            elif action == 'move_forward':
                return self.move_forward
            elif action == 'grab':
                return self.grab
            elif action == 'shoot':
                return self.shoot
            elif action == 'climb':
                return self.climb

        self.kb.tell(f"Performed action: {action}")
        self.time += 1
        print(f"Time: {self.time}")
        return action
