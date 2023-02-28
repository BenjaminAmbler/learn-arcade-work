"""
This is a mini text adventure game for Lab 6.
Created 2/23/2023 by Benjamin Vincent Ambler
Here is the room layout for Lab 6 in the book.

       N
       |
W _____|_____ E
       |
       |
       S

                 ___________________
                |                   |
               |       Balcony       |
               |       Room 6        |
                |                   |
 _______________|_______]   [______|____________________
|               |                   |                   |
|   Bedroom 1   |_   North Hall     |_     Kitchen      |
|    Room 3     _     Room 4        _       Room 5      |
|               |                   |                   |
|_______________|_______]   [_______|_______]   [_______|
|               |                   |                   |
|   Bedroom 2   |_    South Hall    |_    Dining Room   |
|       0       _          1        _         2         |
|               |                   |                   |
|_______________|___________________|___________________|

"""

"""
Define a class called Room
"""
class Room:
    """
    This is a class that represents a room
    """
    def __init__(self, description, objects, north, east, south, west):
        """ This is a method that sets up the variables in the object,
         in this case, the room I think? Need to ask Scott. """
        self.description = description
        self.objects = objects
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    """ Create an empty list called room_list so that you can append to it """
    room_list = []
    # current_room = []


    """ This creates the rooms
    first, creating room 0 which is Bedroom 2. """
    my_room = Room("You are in Bedroom 2. There is a room to the east.",
                   "objects",
                   None,
                   1,
                   None,
                   None)
    room_list.append(my_room) # this adds this room to the room_list
    """ Next, creating room 1 which is the South Hall """
    my_room = Room("South Hall",
                   "objects",
                   4,
                   2,
                   None,
                   0)
    """ Next, creating room 2 which is the Dining Room """
    my_room = Room("Dining Room",
                   "objects",
                   5,
                   None,
                   None,
                   1)
    """ Next, creating room 3 which is Bedroom 1 """
    my_room = Room("Dining Room",
                   "objects",
                   None,
                   4,
                   None,
                   None)
    """ Next, creating room 4 which is the North Hallway """
    my_room = Room("North Hallway",
                   "objects",
                   6,
                   5,
                   1,
                   3)
    """ Next, creating room 5 which is the Kitchen """
    my_room = Room("kitchen",
                   "objects",
                   None,
                   None,
                   2,
                   4)
    """ Next, creating room 6 which is the Balcony """
    my_room = Room("balcony testing testing, is this the room description?",
                   "objects",
                   None,
                   None,
                   4,
                   None)

    print(my_room.description)
    room_list.append(my_room)
    for indx,cur_room in enumerate(room_list):
        print('index:',indx)
        print("Room Description", cur_room.description)
        if cur_room.east is not None:
            print("To the East:",room_list[cur_room.east].description)


""" trying to append this room to the room list """
current_room = 0



""" call or run the main function.
Only run the main function if we are running this file.
Don't run it if we are importing this file. """
if __name__ == "__main__":
    """ print("hello") """
    main()