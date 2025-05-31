class Vacuum:
    """
    A simple robot vacuum that can move left if a location is dirty or else move right.
    """

    def __init__(self):
        """
        Initializes the vacuum's position and the set of cleaned locations.
        """
        self.position = 0
        self.cleaned_locations = set()

    def move_left(self):
        """
        Move the vacuum one position to the left.
        """
        self.position = self.position - 1

    def move_right(self):
        """
        Move the vacuum one position to the right.
        """
        self.position = self.position + 1
    
    def is_dirty(self, location):
        """
        A given location is dirty or not by checking if it marks in cleaned locations.
        return: True if the location is dirty, False if it has been cleaned.
        """
        return location not in self.cleaned_locations

    def clean(self, location):
        """
        Clean the given location by marking it as cleaned.
        Then add it in cleaned locations.
       
        """
        self.cleaned_locations.add(location)

    def action(self, location):
        """
        Perform the right action based on the cleanliness of the location.
        
        If the location is dirty, clean it; if it is clean, move the vacuum right.
        
        return: A string indicating the action taken ("Clean" or "Already Clean").
        """
        if self.is_dirty(location):
            self.clean(location)
            return "Clean"
        else:
            self.move_right()
            return "Already Clean"
