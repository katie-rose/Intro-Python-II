# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, locations):
        self.locations = locations

    def travel(self, direction):
         # Move player toward a room. Returns True on success, 
         # False on failure
        targetRoom = getattr(self.locations)
        if targetRoom:
            self.locations = targetRoom
            return True
        else:
            return False
