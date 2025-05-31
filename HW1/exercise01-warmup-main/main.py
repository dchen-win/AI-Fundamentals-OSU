# Vacuum Scratchpad
# Cindy Chen
# Use this as a "scratchpad" to tinker with your Vacuum objects.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from vacuum import Vacuum

rooms = {
    "Room A": "dirty",  # Room A is dirty
    "Room B": "clean",  # Room B is already clean
    "Room C": "dirty",  # Room C is dirty
    "Room D": "dirty",  # Room D is dirty
    "Room E": "clean",  # Room E is already clean
}

vacuum = Vacuum()

print("Starting vacuum simulation\n")

for idx, (room, status) in enumerate(rooms.items()):
    print(f"Vacuum is at {room}.")

    
    if status == "clean":
        vacuum.cleaned_locations.add(room)  
        print(f"{room} is clean.")
    else:
        print(f"{room} is dirty.")

  
    action = vacuum.action(room)
    print(f"Vacuum action: {action}")


    if idx < len(rooms) - 1:
        vacuum.move_right()
        print(f"Vacuum moved to position {vacuum.position}.\n")
    else:
        print("Vacuum simulation completed.\n")
