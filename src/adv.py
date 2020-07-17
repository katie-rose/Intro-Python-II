from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What do they call you around these parts?")

Katie = Player("Katie",room['outside'])
currentLocation = None

print("To play, use w, n, e, s to navigate West, North, East or South. Press q at any time to quit")

playing = True
while playing:
    for key, value in room.items():
        if value.name == Katie.location.name:
            print(value)
            currentLocation = value
    move = input("\nWhich direction should we go?")
    if move == "n":
        if Katie.location.n_to == None:
            print("\nWe can't go there")
        else:
            Katie.location = Katie.location.n_to
    if move == "s":
        if Katie.location.s_to == None:
            print("\nWe can't go there!")
        else:
            Katie.location = Katie.location.s_to
            print
    if move == "e":
        if Katie.location.e_to == None:
            print("\nWe can't go there!")
        else:
            Katie.location = Katie.location.e_to
    if move == "w":
        if Katie.location.w_to == None:
            print("\nWe can't go there!")
        else:
            Katie.location = Katie.location.w_to
    if move == "q":
        print(
            f"\n Bye")
        playing = False


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
