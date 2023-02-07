""" This is a camel running through the desert while being
chased text based game written by Ben Ambler 2/6/2023 """

import random
def print_instructions():
    """ This function prints the instructions """

    print("""
    Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.
    """)

    """ Creating a Boolean value called done and setting it to False """

def get_player_choice():
        """ Get the player's choice """
        print("""       A. Drink from your canteen. 
                        B. Ahead moderate speed.
                        C. Ahead full speed.
                        D. Stop for the night.
                        E. Status check.
                        Q. Quit.""")
        # Keep looking until someone wins
        done = False
        while not done:
            # Loop for each player
            for player_choice in player_names:
                # Process their turn
                done = process_player_turn(player_name, distance_apart)
                # If someone won, 'break' out of this loop and end the game.
                if done:
                    break

def main():
    """ Main Program """
    print_instructions()
    get_player_choice()


if __name__ == "__main__":
    main()