""" This is a camel running through the desert while being
chased text based game written by Ben Ambler 2/6/2023 """

import random
'''
def print_instructions():
    """ This function prints the instructions """

    print("""
    Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.
    """)
'''
'''
def print_choices():
    print("""       
                    A. Drink from your canteen. 
                    B. Ahead moderate speed.
                    C. Ahead full speed.
                    D. Stop for the night.
                    E. Status check.
                    Q. Quit.""")
'''
# set your variables
miles_traveled = 0
thirst = 0
camel_tiredness = 0
miles_natives_traveled = -20
drinks_left_in_canteen = 3
oasis = 0

# print_instructions():

print("""
    Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.""")

# get_player_choice():
done = False
while not done:
    print("""       
                    A. Drink from your canteen. 
                    B. Ahead moderate speed.
                    C. Ahead full speed.
                    D. Stop for the night.
                    E. Status check.
                    Q. Quit.
    """)
    player_choice = input("What is your choice? ")

    if player_choice.upper() == "Q":
        done = True

    elif player_choice.upper() == "E":
        print("You've gone this far:", miles_traveled)
        print("You've got this many drinks left:", drinks_left_in_canteen)
        print("The natives are", miles_traveled - miles_natives_traveled, "miles back ")
        print("Your camel tiredness is", camel_tiredness)
        print("You are now this thirsty", thirst)

    elif player_choice.upper() == "D":
        camel_tiredness = 0
        print("Your camel yawns, stretches, and looks happy and refreshed")
        miles_natives_traveled = miles_natives_traveled + random.randrange (7,15)

    elif player_choice.upper() == "C":
        miles_traveled = miles_traveled + random.randrange (10, 21)
        print("you traveled", miles_traveled, "miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange (1,4)
        miles_natives_traveled = miles_natives_traveled + random.randrange (7, 15)
        print("You are now", miles_traveled - miles_natives_traveled, "miles ahead of the natives")

    elif player_choice.upper() == "B":
        miles_traveled = miles_traveled + random.randrange(5, 13)
        print("you traveled", miles_traveled, "miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1, 4)
        miles_natives_traveled = miles_natives_traveled + random.randrange(7, 15)

    elif player_choice.upper() == "A":
        if drinks_left_in_canteen > 0:
            drinks_left_in_canteen = drinks_left_in_canteen - 1
            thirst = 0
            print("""
                    You carefully take a sip from your canteen, being extra careful
                    to not spill even a single drop. 
                    Your thirst is quenched and you feel refreshed. """)
        elif drinks_left_in_canteen == 0:
            print(""" You are all out of water... this is not good. """)
    if done == False and miles_natives_traveled >= miles_traveled:
        print(" The natives caught you. Game over.")
    if done == False and camel_tiredness > 8:
        print("Your camel died. Game over.")
        done = True
    elif done == False and camel_tiredness > 5:
        print("Your camel is getting tired")
    if thirst > 6:
        print(" You died of thirst. Game over.")
        done = True
    elif done == False and thirst > 4:
        print(" You are very thirsty." )
    if done == False and miles_traveled <= miles_natives_traveled + 15:
        print(" The natives are getting close! ")
    if done == False and miles_traveled >= 200:
        print("You beat the game! Well done!")
    if done == False and random.randint(0, 20) == 10:
        camel_tiredness = 0
        drinks_left_in_canteen = 3
        print("You found and oasis! Your camel is refreshed and your canteen is refilled.")


'''
def main():
    """ Main Program """
    print_instructions()
    print_choices()
    get_player_choice()


if __name__ == "__main__":
    main()
'''