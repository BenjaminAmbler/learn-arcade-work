#
# Lab 10
# How many words are misspelled in the first 200 words
# of the book Alice In Wonderland
# Trying to follow the instructions found here:
# https://learn.arcade.academy/en/latest/labs/lab_10_spell_check/spell_check.html
#

# Steps 1-4, download the dictionary file and the alice in wonderland file
# and put them in the same directory as this program. Done.

# Step 5, import re which stands for regular expression. Next, use this function
# which takes in a line of text and returns
# a list of words from that line, but now the words are stripped of any
# extra punctuation.l

import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# Step 6, read the dictionary file into an array

""" Read in lines from the dictionary file """

# Open the file for reading, and store a pointer to it in the new
# variable which is called dictionary_file
dictionary_file = open("dictionary.txt")

    # Create an empty list to store our dictionary words in
words_in_dictionary_list = []

    # Loop through each line in the dictionary_file like a list
for line in dictionary_file:
    for line in dictionary_file:
        words_in_dictionary_list.append(line.strip())
    # Step 7, don't forget to close the file since this is best practice
    # and doesn't lead to depending on your operating system which
    # may or may not close the file eventually
dictionary_file.close()

    # uncomment the line below to print out how many words are in the
    # dictionary to be able to see if this thing is working so far:
    # print("There are", len(words_in_dictionary_list), "words in this dictionary file.")
    # return words_in_dictionary_list

# Step 8, print --- Linear Search ---
print(" --- Linear Search --- ")

# Step 9, open the file AliceInWonderLand200.txt
alice_in_wonderland_file = open("AliceInWonderLand200.txt")

# Step 10, we are not going to create an empty list to put this in like
# we did for the dictionary, per the instructions.

    # Step 11, start a for loop to iterate through each line one by one
for number, line in enumerate (alice_in_wonderland_file):

# Step 12, call the split line function to split apart the line of text
# in the story that was just read in. Store the list that the function returns
# into a new variable named word_list.
    word_list = split_line(line)

        # Step 13 start a nested for loop to iterate through each word in the
        # word list. This should be inside of the for loop that runs through
        # each line in the file. (One loop for each line, another loop for
        # each word in the line)
    for word in word_list:
    # Step 14, using a linear search, check the current word against the words in the
    # dictionary. See Linear Search Algorithm for example code on how to do this.
    # The linear search is just three lines long. When comparing to the word to the other
    # words in the dictionary, convert the word to uppercase. In your while loop just use
    # word.upper() instead of word for the key. This linear search will exist inside the
    # for loop created in the prior step. We are looping through each word in the dictionary,
    # looking for the current word in the line that we just read in.
        # --- Linear search

        word = word.upper()

        # Start at the beginning of the list
        current_list_position = 0

        # Loop until you reach the end of the list, or the value at the
        # current position is equal to the word
        while current_list_position < len(words_in_dictionary_list) \
                and words_in_dictionary_list[current_list_position] != word.upper():
                # Advance to the next item in the list
                current_list_position += 1

        if current_list_position == len(words_in_dictionary_list):
            print(f"The word at line {number + 1}, "
                  f"is either a misspelled word, or would you like to add it to the dictionary?:{word}")
        #     print("The word is at position", current_list_position)
        # else:
        #     print("The word was not in the dictionary.")

alice_in_wonderland_file.close()




