#
# Linear Search Example
#


import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """ Read the dictionary into an array """

    # Open the file for reading, and store a pointer to it in the new
    # variable "my_dictionary_file"
    dictionary_file = open("dictionary.txt")

    # Create an empty list to store our words from the dictionary
    dictionary_list = []

    dictionary_file.close()

    print( "Linear Search,"
           " there are this many words in my dictionary file: ", len(dictionary_list))

    # # Loop through each line in the file like a list
    # for line in dictionary_file:
    #     # call the split line function to separate the words
    #     # individually in the dictionary
    #     line = split_line(dictionary_list)
    #
    #     # Add the word to the list
    #     dictionary_list.append(line)

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    story_file = open("AliceInWonderLand200.txt")

    # Loop through each line in the file like a list
    for line in story_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        word_list.append(line)

    story_file.close()

    print("There were", len(word_list), "words in the file.")

    # --- Linear search
    key = "what do you want to search for?"

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(word_list) and word_list[current_list_position] != key:
        # Advance to the next item in the list
        current_list_position += 1

    if current_list_position < len(word_list):
        print("The word is at position", current_list_position)
    else:
        print("The word was not in the list.")

main()