#!/usr/bin/env python3

"""
22a368a2e9184c86813e31f6d229cea1
python
lab5
v4
lash23
2024-12-02 09:22:04
v4.0.0 (2019-03-05)

Generated 2024-12-02 10:22:04 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Ross, Chandler, Monica
#
# and corresponding numbers
#
# > 55523645, 55564452, 55545872
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Create the phonebook dictionary
phonebook = {
    "Ross": 55523645,
    "Chandler": 55564452,
    "Monica": 55545872
}

#Answer with the resulting dictionary
ANSWER = phonebook


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#




ANSWER = len(phonebook)


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Monica'.
#
# Write your code below and put the answer into the variable ANSWER.
#


# Use the `get()` method on your phonebook

ANSWER = phonebook.get("Monica")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = sorted(phonebook.keys())

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = sorted(phonebook.values())

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Monica' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = 'Monica' in phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Monica' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#


# Create a copy of the phonebook dictionary.
phonebook_copy = phonebook.copy()

# Remove 'Monica' from the copied phonebook
phonebook_copy.pop('Monica')


ANSWER = phonebook_copy


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with the values 'moose, 12, 1.98, table, 7'. Answer with the
# length of the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Create the tuple
tup = ('moose', 12, 1.98, 'table', 7)

# Get the length of the tuple
ANSWER = len(tup)



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (moose, 12, 1.98, table, 7).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#



# Create the tuple
tup = ('moose', 12, 1.98, 'table', 7)

# Unpack the tuple into variables
a, b, c, d, e = tup


ANSWER = d




# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [67, 50, 2, 39, 15]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#


my_list = [67, 50, 2, 39, 15]

# Create a tuple from the first two elements using slicing
my_tuple = tuple(my_list[:2])

# Set the first element of the tuple as the answer
ANSWER = my_tuple[0]




# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (567, 23, 12, 36, 7)
#
# Convert it to a list and replace the second element with:
#
# > 2286
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Create the tuple
my_tuple = (567, 23, 12, 36, 7)

# Convert the tuple to a list
my_list = list(my_tuple)

# Replace the second element with 2286
my_list[1] = 2286

# Convert the list back to a tuple
my_tuple = tuple(my_list)

#answer with the first three elements in a comma-separated string
ANSWER = f"{my_tuple[0]},{my_tuple[1]},{my_tuple[2]}"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Original phonebook dictionary
phonebook = {
    "Ross": 55523645,
    "Chandler": 55564452,
    "Monica": 55545872
}

# Create a string to store the result
ANSWER = ""


for name in sorted(phonebook.keys()):
    ANSWER += f"{name} {phonebook[name]}\n"




# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#



phonebook = {
    "Ross": 55523645,
    "Chandler": 55564452,
    "Monica": 55545872
}

# Create a new dictionary with updated phone numbers
ANSWER = {}

# Add the prefix '+1-' to each phone number and convert to string
for name, number in phonebook.items():
    ANSWER[name] = '+1-' + str(number)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
