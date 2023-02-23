"""
This is a mini text adventure game for Lab 6.
Created 2/23/2023 by Benjamin Vincent Ambler

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
|_____]   [_____|_______]   [_______|_______]    [______|_____________
|                                                                     )
| W Hallway 3     Central H way 4     East Hallway 5      Balcony 6    )
|                                                                      )
|_____]   [_____________]   [_______________]    [____________________)
|               |                   |                   |
|   Game Room   |       Kitchen     |     Dining Room   |
|       0       |          1        |         2         |
|               |                   |                   |
|_______________|___________________|___________________|



"""

"""
Define a class called Room as shown in Defining the Class
"""
class Room:
    """
    This is a class that represents a room
    """
    def __init__(self, description, objects, north, east, south, west):
        """ This is a method that sets up the variables in the object,
         in this case, the room I think? Need to ask Scott. """
        self.description = ""
        self.objects = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0


def main():
    """ Create an empty list """
    empty_list = []
    """ This creates the room """
    my_room = Room("description",
                   "objects",
                   "north",
                   "east",
                   "south",
                   "west")


""" call or run the main function.
Only run the main function if we are running this file.
Don't run it if we are importing this file. """
if __name__ == "__main__":
    main()


""" 

Step 7: Create a variable called room. Set it equal to a new instance of the Room class.
For the first parameter, create a string with a description of your first room. 
The last four elements will be the number of the next room if the user goes
north, east, south, or west. Look at your sketch to see what numbers to use. 
Use None if no room hooks up in that direction. (Do not put None in quotes. 
Also, remember that Python is case sensitive so none won’t work either. 
The keyword None is a special value that represents “nothing.” 
Because sometimes you need a value, other than zero, that represents )

"""

room = (Room)

""" oh boy, going to need some serious help with this one. """

