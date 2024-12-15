#!/usr/bin/env python3

"""
83c519693c393f65e82649cac1d308a7
python
lab2
v4
lash23
2024-09-19 14:53:20
v4.0.0 (2019-03-05)

Generated 2024-09-19 16:53:20 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 5, `dice2` = 6
# and `dice3` = 3.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 5
dice2 = 6
dice3 = 3




ANSWER = dice1> dice2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 5
dice2 = 6
dice3 = 3

total = dice1 + dice2 + dice3

# Check if the total is greater than 11
if total > 11:
    result = 'big'  
else:
    result = 'small' 


ANSWER = result 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 6 and `dice5` = 2 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#
dice1 = 5
dice2 = 6
dice3 = 3
dice4 = 6
dice5 = 2 

# Calculate the total sum of all dice
total_sum = dice1 + dice2 + dice3 + dice4 + dice5

# Use if, elif, else to check the total value of the dice sum
if total_sum < 11:
    ANSWER = 'small'
elif 11 <= total_sum < 21:
    ANSWER = 'intermediate'
else:
    ANSWER = 'big'

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'restaurant'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Create the variable summer_word
summer_word = 'restaurant'

# Check if 's' is in summer_word
answer = 's' in summer_word


ANSWER = answer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#


# Initialize an empty string
result =""
# Loop through the numbers 0 to 10
for number in range(11):
# result = result + str(number)+ "," # Convert number to string and add a comma

    result = f"{result}{number}," 
ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#


summer_word = 'restaurant'

# Define a string of consonants
consonants = 'bcdfghjklmnpqrstvwxyz'

# Initialize an empty string to store the result
result = ''

# Loop through each letter in summer_word
for letter in summer_word:
    if letter in consonants:  # Check if the letter is a consonant
        result += letter       # Concatenate the consonant to result






ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 18 to 74 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#


# Initialize a variable to store the sum of odd numbers
sum_of_odds = 0

# Loop through the numbers from 18 to 74
for i in range(18, 75):
    if i % 2 != 0:  # Check if the number is odd
        sum_of_odds += i  # Add the odd number to the sum




ANSWER = sum_of_odds


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 8 and ends when the value is
# greater than 20, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

increment = 8
result = ''
while increment <= 20:
    result = f"{result}{increment},"
    increment = increment + 3


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 4 from 61, 60 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

value = 61

# Initialize the counter for the loop
counter = 0

# Create the while loop that runs 60 times
while counter < 60:
    value -= 4  # Subtract 4 from value
    counter += 1  # Increment the counter




ANSWER = value

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 12, 12!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 12 is `12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 *
# 4 * 3 * 2 * 1`. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Initialize the value for which we want the factorial
number = 12

# Initialize a variable to store the result of the factorial calculation
factorial = 1

# Create a while loop that multiplies the factorial by decreasing values of number
while number > 1:
    factorial *= number  # Multiply factorial by the current number
    number -= 1  # Decrease the number by 1






ANSWER = factorial

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'philanthropist'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#


# Define the word to be reversed
word = 'philanthropist'

# Initialize an empty string to store the reversed word
reversed_word = ''

# Use a for-loop to iterate through the word in reverse order
for letter in word:
    reversed_word = letter + reversed_word  



ANSWER = reversed_word 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers (Not using
# new plates which can have more letters). The numbers range from 001 to 999.
# Using one of the four common rules of arithmetics (+, -, *, /), on how many
# of the numberplates can the two first numbers give the third number? We
# only care about the numbers, we ignore letters for this assignment.
#
# Alternatives:
# a + b = c
# a - b = c
# a * b = c
# a / b = c
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Examples:
# '123' can be combined to 1 + 2 = 3. So this numberplate is good. Since this
# matched on + operator, we don't continue checking with the other operators.
# '129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

# Initialize the counter for valid number plates
valid_count = 0

# Loop through all possible number plates from 001 to 999
for number in range(1, 1000):
    # Convert the number to a zero-padded string (e.g., 001, 123)
    plate = str(number).zfill(3)
    
    # Extract the digits a, b, and c from the number plate
    a = int(plate[0])
    b = int(plate[1])
    c = int(plate[2])
    
    # Check if any of the arithmetic operations between a and b result in c
    if a + b == c:
        valid_count += 1
    elif a - b == c:
        valid_count += 1
    elif a * b == c:
        valid_count += 1
    elif b != 0 and a / b == c:
        valid_count += 1


ANSWER = valid_count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
