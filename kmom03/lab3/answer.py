"""
This module contains functions for:
- Validating passwords according to specified criteria.
- Counting the number of vowels in a given string.
- Analyzing passwords and reporting their validity and vowel count.

It includes the following functions:
- valid_password: Checks if a password meets criteria for validity.
- number_of_vowels: Counts vowels in a string.
- analyze_password: Combines the above functionalities to analyze a password.
"""
import functions
from dbwebb import Dbwebb
#!/usr/bin/env python3

"""
99f5fbab223e8b78b57d42ee599a3984
python
lab3
v4
lash23
2024-09-26 18:42:27
v4.0.0 (2019-03-05)

Generated 2024-09-26 20:42:27 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'AP4ssword'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def valid_password(password):
    """
    Check whether the provided password meets the following criteria:
    
    - Is 8 characters or longer
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    is_upper = False
    is_lower = False
    is_digit = False
    
    if len(password) < 8:
        return False
    
    for char in password:
        if char.isupper():
            is_upper = True
        if char.islower():
            is_lower = True
        if char.isdigit():
            is_digit = True

    return is_upper and is_lower and is_digit


ANSWER = valid_password('AP4ssword')



# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'secretpassw0rd'.
#
# Write your code below and put the answer into the variable ANSWER.
#




# Assign the result of valid_password to ANSWER
ANSWER = valid_password('secretpassw0rd')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy. Your solution should be
# case-insensitive.
#
# Answer with the number of vowels in the following text:
#
# 'Stoicism has just a few central teachings. It sets out to remind us of how
# unpredictable the world can be.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(input_text):
    """
    Count the number of vowels in the given text.
    
    Args:
        input_text (str): The text to analyze for vowels.
    
    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouyAEIOUY"
    count = 0


    for char in input_text:
        if char in vowels:
            count += 1

    return count

# Given text to analyze
text_to_analyze = (
    'Stoicism has just a few central teachings. '
    'It sets out to remind us of how unpredictable '
    'the world can be.'
)

ANSWER = number_of_vowels(text_to_analyze)




# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# Example: With the input value anoth3ePw0Rd the function should return the
# following string: 'anoth3ePw0Rd is a valid password and contains 3
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: AP4ssword.
#
# Write your code below and put the answer into the variable ANSWER.
#


def analyze_password(password):
    """
    Analyze the given password and return a string indicating its validity
    and the number of vowels it contains.

    Args:
        password (str): The password to analyze.

    Returns:
        str: A message indicating whether the password is valid and the 
             count of vowels.
    """
    is_valid = valid_password(password)
    vowel_count = number_of_vowels(password)
    
    validity_string = "is a valid password" if is_valid else "is not a valid password"
    return f"{password} {validity_string} and contains {vowel_count} vowels."

# Example usage
ANSWER = analyze_password('AP4ssword')




# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `multiplication` that takes
# two arguments. The function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 47 and 6.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = functions.multiplication(47, 6)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'beach' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = functions.funny_word('beach')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `decider`. The function takes
# one argument. If the argument is a string return a call to `funny_word()`,
# if the argument is an integer return the square of the argument by using
# the `multiplication` function.
#
# Answer with a call to the function `decider` with the value `84` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = functions.decider(84)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# 'blunderbuss' and 82 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#




ANSWER = functions.double_decider('blunderbuss', 82)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

dbwebb.exit_with_summary()
