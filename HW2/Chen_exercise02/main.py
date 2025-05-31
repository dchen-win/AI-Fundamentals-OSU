# Main
# YOUR NAME
# The start of your overall agent program.
# Demonstrate the use of your SimpleReflexVacuum and your ModelReflexVacuum.
# The code for using a SimpleReflexVacuum is provided for you.


# Part 1


from location import Location
from state import State
from movement_model import MovementModel
from transition_model import TransitionModel
from sensor_model import SensorModel

from simple_reflex_vacuum import SimpleReflexVacuum

simple_reflex_vacuum = SimpleReflexVacuum()
action = simple_reflex_vacuum.action('A', 'Dirt')
action()



# Part 2

from model_reflex_vacuum import ModelReflexVacuum

vacuum_world = State({'A': Location('A', True), 'B': Location('B', None)}, 'B')
movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
transition_model = TransitionModel(vacuum_world, movements)
sensor_model = SensorModel(vacuum_world)

model_reflex_vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
action = model_reflex_vacuum.action()

print(f'Action taken: {action}')
a = vacuum_world.locations['A'].dirt
b = vacuum_world.locations['B'].dirt
print(f'Status location A: {a}')
print(f'Status location B: {b}')
print(f'Vacuum world (State): {vacuum_world.locations}')



