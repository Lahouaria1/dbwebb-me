"""
This module contains several utility functions including:
- multiplication: Multiplies two numbers.
- funny_word: Prepends a string with a phrase.
- decider: Decides based on the input type (string or integer).
- double_decider: Processes two arguments using the decider function.
"""

def multiplication(num1, num2):
    """
    Multiply two numbers.

    Args:
        num1 (int, float): The first number.
        num2 (int, float): The second number.

    Returns:
        int, float: The product of num1 and num2.
    """
    return num1 * num2

def funny_word(word):
    """
    Create a string by appending ' is a funny word'.

    Args:
        word (str): The word to prepend.

    Returns:
        str: A string formatted as '<word> is a funny word'.
    """
    return f"{word} is a funny word"

def decider(value):
    """
    Decide the action based on the type of value.

    If the value is a string, it returns a funny word. 
    If it is an integer, it returns the square of that integer.

    Args:
        value (str, int): The input value.

    Returns:
        str, int: A funny word or the square of the integer, or None for unsupported types.
    """
    if isinstance(value, str):
        return funny_word(value)
    if isinstance(value, int):
        return multiplication(value, value)
    return None  # Handle unsupported types

def double_decider(arg1, arg2):
    """
    Process two arguments and return their results.

    Calls the decider function on both arguments and formats the results.

    Args:
        arg1 (str, int): The first argument.
        arg2 (str, int): The second argument.

    Returns:
        str: A concatenated result of the two decider calls.
    """
    result1 = decider(arg1)
    result2 = decider(arg2)
    return f"{result1} and the square is {result2}"
