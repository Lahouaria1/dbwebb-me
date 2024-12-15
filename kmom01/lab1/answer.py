#!/usr/bin/env python3

"""
808de3d8f49abb360a402a7952a91348
python
lab1
v4
lash23
2024-09-07 19:09:38
v4.0.0 (2019-03-05)

Generated 2024-09-07 21:09:38 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 100.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#



num_one = 100


ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 88. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 88

result = num_one + num_two


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 13.
#
# Create another variable called `num_four` and give it the value 74.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_three = 13
num_four = 74
subtraction_result = num_four - num_three
final_result = result + subtraction_result



ANSWER = final_result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = num_one * num_three


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 34.01.
#
# Create another variable called `float_two` and give it the value 31.83.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#


float_one = 34.01
float_two = 31.83
result = round(float_one + float_two, 2)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`. Use the function
# `round()` to round the number to two decimals.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


result = num_three + num_one - num_four
second_result = result * num_two + float_two - float_one
final_result = round(second_result, 2)


ANSWER = final_result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'screen' and 'water' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


result = "screen" + "water"



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'water' with the integer 100, with a space between the
# two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#


new_string = "water" + " " + str(100)



ANSWER = new_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 100 with the word 'screen' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 88 and the word 'water' with a space between between
# the two values.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = str(100) + ' screen' + ' and ' + str(88) + ' water'

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = int(30)
actual_number = 5
divide = string_number / actual_number

ANSWER = round(divide)



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
# BTH is using a wind-turbine and solar panels to harvest energy from the
# wind and sun. On a windy and sunny day in September the sun shines for 10
# hours with an average output effect of the solar panels of 9345 W per hour.
# The wind turbine has an average output effect of 314 W per hour for all 24
# hours of the day.
#
# Calculate the total output energy i kWh from the wind turbine and the solar
# panels for the entire day.
#
# Energy i kWh is calculated as `energy = effect * hours / 1000`.
#
# Write your code below and put the answer into the variable ANSWER.
#
effect_solar = 9345  # W per hour for the solar panels
hours_sunshine = 10  # hours of sunshine
effect_wind = 314    # W per hour for the wind turbine
hours_wind = 24      # hours of wind

# Calculate energy from solar panels
energy_solar = effect_solar * hours_sunshine / 1000  # kWh

# Calculate energy from wind turbine
energy_wind = effect_wind * hours_wind / 1000  # kWh

total_energy = energy_solar + energy_wind





ANSWER = total_energy

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#

peter_phonenumber = '0731415926'
anna_phonenumber = '0727182818'
minutes_per_call = 9  # minutes per call
sundays_per_year = 52

# Calculate total minutes per year
total_minutes_per_year = minutes_per_call * sundays_per_year

# Convert to hours
total_hours_per_year = total_minutes_per_year / 60


ANSWER = (
    f"Peter calls from {peter_phonenumber} to Anna on {anna_phonenumber} "
    f"for {total_hours_per_year} hours every year."
)
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
