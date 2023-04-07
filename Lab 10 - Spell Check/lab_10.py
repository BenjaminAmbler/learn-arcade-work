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

def main():
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

    print( "There were", len(words_in_dictionary_list), "words in the dictionary file.")


main()