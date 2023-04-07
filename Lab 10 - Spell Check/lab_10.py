#
# Linear Search Example
# Lab 10
# How many words are misspelled in the first 200 words
# of the book Alice In Wonderland
#


import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_dictionary():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    dictionary_file = open("dictionary.txt")

    # Create an empty list to store our names
    words_in_dictionary_list = []

    # Loop through each line in the file like a list
    for line in dictionary_file:

        # Add the name to the list
        words_in_dictionary_list.append(line)

    dictionary_file.close()

    # uncomment the line below to print out how many words are in the
    # dictionary to be able to see if this thing is working so far:
    print("There are", len(words_in_dictionary_list), "words in this dictionary file.")

    #return words_in_dictionary_list

print( " --- Linear Search --- " )
alice_in_wonderland_file = open("AliceInWonderLand200.txt")
# do not create an empty list to put this in like we did for the dictionary,
# per the instructions on step 10 here:
# https://learn.arcade.academy/en/latest/labs/lab_10_spell_check/spell_check.html

    # step 11
    for line in alice_in_wonderland_file:
        return = split_line:






