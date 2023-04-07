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
    # print( "There are", len(words_in_dictionary_list), "words in this dictionary file.")

    return words_in_dictionary_list

def linear_search(key, words_in_dictionary_list):
    """ Linear search """

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(words_in_dictionary_list) and words_in_dictionary_list[current_list_position] != key:

        # Advance to the next item in the list
        current_list_position += 1

    return current_list_position


def main():

    key = "Morgiana the Shrew"
    words_in_dictionary_list = read_in_dictionary("dictionary.txt")
    list_position = linear_search(key, words_in_dictionary_list)

    if list_position < len(words_in_dictionary_list):
        print("The name", key, "is at position", list_position)
    else:
        print("The name", key, "was not in the list.")


main()