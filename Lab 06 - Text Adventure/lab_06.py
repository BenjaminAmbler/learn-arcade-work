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
    done = False
    room_list = []
    current_room = 0


    """ This creates the rooms
    first, creating room 0 which is Bedroom 2. """
    my_room = Room("You are in Bedroom 2. There is a room to the east.",
                   "objects", # we can add keys or something here as an object later
                   None, # this is set to None since there is no door to the north
                   1, # this is set to 1 since
                   None, # this is set to None since there is no room to the south
                   None) # no doorway to the west in this room
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 1 which is the South Hall """
    my_room = Room("You are in the South Hall. There is a door to the west and to the east.",
                   "objects",
                   4,
                   2,
                   None,
                   0)
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 2 which is the Dining Room """
    my_room = Room("You are in the Dining Room. There is a door to the north and to the west",
                   "objects",
                   5,
                   None,
                   None,
                   1)
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 3 which is Bedroom 1 """
    my_room = Room(" You are in Bedroom 1. There is a door to the east.",
                   "objects",
                   None,
                   4,
                   None,
                   None)
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 4 which is the North Hallway """
    my_room = Room(" You are in the North Hallway. There is a door in every direction.",
                   "objects",
                   6,
                   5,
                   1,
                   3)
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 5 which is the Kitchen """
    my_room = Room(" You are in the Kitchen. There is a door to the south and to the west",
                   "objects",
                   None,
                   None,
                   2,
                   4)
    room_list.append(my_room) # this adds this room to the room_list

    """ Next, creating room 6 which is the Balcony """
    my_room = Room(" You are on the Balcony ",
                   "objects",
                   None,
                   None,
                   4,
                   None)
    room_list.append(my_room) # this adds this room to the room_list

    # print(room_list[current_room].description)
    # print(current_room)

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice: str = input("Which direction do you want to go? I understand N,E,S,W. N = north, E = east, S = south, W = west. q to quit"
                                 "\nWhat is your choice? : ")
        my_result = user_choice.upper() == "N, E, S, W"
        if user_choice.upper() == "N":
            next_room = room_list[current_room].north

        elif user_choice.upper() == "E":
            next_room = room_list[current_room].east

        elif user_choice.upper() == "S":
            next_room = room_list[current_room].south

        elif user_choice.upper() == "W":
            next_room = room_list[current_room].west

        elif user_choice.upper() == "Q":
            print("Thanks for playing Ben's Text Adventure Game")
            break

        if next_room == None:
            print(" \nYou hear a computer voice say: \n \"Error, Error, does not compute, \n you can not go that way beep boop..."
                  " \n there is no door that in that direction"
                  " \n or I do not understand that input"
                  " \n beep boop please try again\"")
        else:
            current_room = next_room


    # print(my_room.description)
    # #room_list.append(my_room)
    # for indx,cur_room in enumerate(room_list):
    #     print('index:',indx)
    #     print("Room Description", cur_room.description)
    #     if cur_room.east is not None:
    #         print("To the East:",room_list[cur_room.east].description)



""" call or run the main function.
Only run the main function if we are running this file.
Don't run it if we are importing this file. """
if __name__ == "__main__":

    main()