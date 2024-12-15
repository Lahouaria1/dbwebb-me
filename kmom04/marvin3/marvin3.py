#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# marvin2.py
"""
Marvin with a simple menu to start up with.
Marvin provides functions for generating SSNs, acronyms, randomizing strings,
and finding indexes of substrings.
"""

import random
def create_ssn(birth_date):
    """
    Generate the last four digits of the SSN based on a birth date.
    """
    random_numbers = [random.randint(0, 9) for _ in range(3)]
    ssn_without_last_digit = birth_date + ''.join(map(str, random_numbers))
    
    # Calculate the Luhn sum
    total_sum = calculate_luhna_sum(ssn_without_last_digit)
    
    # Calculate the last digit
    last_digit = (10 - (total_sum % 10)) % 10
    full_ssn = f"{birth_date}-{''.join(map(str, random_numbers))}{last_digit}"
    return full_ssn

def calculate_luhna_sum(ssn):
    """Calculate the Luhn sum for a given SSN."""
    total_sum = 0
    for i, digit in enumerate(ssn):
        digit = int(digit)
        if i % 2 == 0:  # If index is even
            digit *= 2
            if digit > 9:  # Sum the digits if > 9
                digit -= 9
        total_sum += digit
    return total_sum

def get_acronym(input_string):
    """Creates an acronym from the uppercase letters of the input string."""
    # Extract uppercase letters and join them to form the acronym
    acronym = ''.join(char for char in input_string if char.isupper())
    return acronym 
    
def randomize_string(input_string):
    """Randomizes the letters in the input string."""
    if not input_string:  # Check if input string is empty
        return "Input string is empty."
    return ''.join(random.sample(input_string, len(input_string)))

def find_all_indexes(main_string, sub_string):
    """
    Finds all starting indexes of sub_string within main_string.
    """
    if not sub_string:  
        return ""  # Return empty string if sub_string is empty
    
    indexes = []  # Initialize an empty list to store indexes
    start = 0  # Starting index for the search
    while True:
        try:
            # Find the next index for the substring, starting from 'start'
            index = main_string.index(sub_string, start)
            indexes.append(index) 
            start = index + 1  # Move start to the next position
        except ValueError:
          
            break
            
    # Convert indexes to strings and join them with commas
    if indexes:
        result = ",".join(str(index) for index in indexes)  # Using join to create the result string
        return result  

    return "" 
