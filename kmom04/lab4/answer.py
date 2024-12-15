#!/usr/bin/env python3

"""
8654d1e3a8c7c63f697e6179cb6b7e1a
python
lab4
v4
lash23
2024-11-20 17:45:31
v4.0.0 (2019-03-05)

Generated 2024-11-20 18:45:31 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [cougar, cougar] and [Whitaker, flute].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Define the two lists
list1 = ["cougar", "cougar"]
list2 = ["Whitaker", "flute"]

# Concatenate the lists
ANSWER = list1 + list2



ANSWER = ['cougar', 'cougar', 'Whitaker', 'flute']
# ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [table, wall, desk, chair, floor].
#
# Add the words 'elevator' and 'bag' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
modified_list = ["table", "wall", "desk", "chair", "floor"]


modified_list.insert(1, "elevator")  # Insert 'elevator' at index 1 (second position)
modified_list.insert(2, "bag")       # Insert 'bag' at index 2 (third position)



ANSWER = modified_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [table, wall, desk, chair, floor].
#
# Replace the third word with: 'painting'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

modified_list = ["table", "wall", "desk", "chair", "floor"]

modified_list[2] = "painting"

ANSWER = modified_list

# ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [flute, guitar, drums, piano, bass]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

sorted_list = ["flute", "guitar", "drums", "piano", "bass"]


ANSWER = sorted(sorted_list, reverse=True)


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'cougar'
#
# from the list:
#
# > [lion, tiger, ozelot, bobcat, cougar]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

modified_list = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

modified_list.remove("cougar")


ANSWER = modified_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#


numbers = [67, 50, 2, 39, 15]
result = sum(numbers)



ANSWER = result 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [123, 4, 125, 69, 155]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

# numbers =[123, 4, 125, 69, 155]
# tot_sum = sum(numbers)
# average= sum(numbers)/len(numbers)

# ANSWER = average
numbers = [123, 4, 125, 69, 155]

# Calculate the total sum and the average
tot_sum = sum(numbers)
average = tot_sum / len(numbers)


ANSWER = float(f"{average:.1f}")



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?snow?is?falling"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

fixed_string= "The?snow?is?falling"


ANSWER = ' '.join(fixed_string.split('?'))

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [pig, horse, cow, cat, dog]
#
# and replace the second and third elements with the elements in the
# following list.
#
# > "green, purple"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

modified_list = ["pig", "horse", "cow", "cat", "dog"]

new_elements = ["green", "purple"]

modified_list[1:3] = new_elements

ANSWER = modified_list



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [e, d, c, b, a]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['e', 'd', 'c', 'b', 'a']
list2 = ['e', 'd', 'c', 'b', 'a']


ANSWER = list1 is list2


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['e', 'd', 'c', 'b', 'a']

list3 = list1

ANSWER = list1 is list3



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "s"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['e', 'd', 'c', 'b', 'a']

list3 = list1
list1[0] = 's'

ANSWER = list3



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [67, 50, 2, 39, 15]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#


def sorted_lists(input_numbers):
    """
    Sorts the input list and multiplies each number by 10.
    """
    input_numbers.sort()
    for i, _ in enumerate(input_numbers):
        input_numbers[i] *= 10
    return input_numbers


numbers = [67, 50, 2, 39, 15]
ANSWER = sorted_lists(numbers)






# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [123, 4, 125, 69, 155]
#
# as argument.
#
# The function should multiply all even numbers by 3 and add 7 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#
def modify_and_sort_list(input_numbers):
    """
    Modifies the input list by multiplying even numbers by 3 and adding 7 to odd numbers.
    The resulting list is then sorted in descending order.
    """
    for index, number in enumerate(input_numbers):
        if number % 2 == 0:
            input_numbers[index] *= 3
        else:
            input_numbers[index] += 7
    input_numbers.sort(reverse=True)
    return input_numbers


numbers = [123, 4, 125, 69, 155]
ANSWER = modify_and_sort_list(numbers)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
