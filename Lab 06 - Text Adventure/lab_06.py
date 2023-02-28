"""
This is a mini text adventure game for Lab 6.
Created 2/23/2023 by Benjamin Vincent Ambler
Maybe I'll create this layout later, for now though,
I'm just going to keep it simple and do the room
layout that is already drawn for Lab 6 in the book.

       N
       |
W _____|_____ E
       |
       |
       S

_________________________________________________________
|               |                   |                   |
|   Man Cave    |   Home Theater    |                   |
|   Room 7      |   Room 8          |      Bedroom 9    |
|               |                   |                   |
|_____]   [_____|_______]   [_______|_______]    [______|____________
|                                                                     )
| W Hallway 3     Central H-way 4     East Hallway 5      Balcony 6    )
|                                                                      )
|_____]   [_____________]   [_______________]    [____________________)
|               |                   |                   |
|   Game Room   |       Kitchen     |     Dining Room   |
|       0       |          1        |         2         |
|               |                   |                   |
|_______________|___________________|___________________|

Ignore this layout above for now.

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
    current_room = []


    """ This creates the rooms
    first, creating room 0 which is Bedroom 2 """
    my_room = Room("Bedroom 2",
                   "objects",
                   None,
                   1,
                   None,
                   None)
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
    print("hello")
    main()