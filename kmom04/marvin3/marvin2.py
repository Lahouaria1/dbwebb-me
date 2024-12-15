#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    random_numbers = ""
    for _ in range(3):
        random_numbers += str(random.randint(0, 9))

    ssn_without_last_digit = birth_date + random_numbers

    total_sum = calculate_luhna_sum(ssn_without_last_digit)

    last_digit = (10 - (total_sum % 10)) % 10
    full_ssn = f"{birth_date}-{random_numbers}{last_digit}"
    return full_ssn


def calculate_luhna_sum(ssn):
    """Calculate the Luhn sum for a given SSN."""
    total_sum = 0
    for i, digit in enumerate(ssn):
        digit = int(digit)
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
    return total_sum


def get_acronym(input_string):
    """Creates an acronym from the uppercase letters of the input string."""
    acronym = ""
    for char in input_string:
        if char.isupper():
            acronym += char
    return acronym


def randomize_string(input_string):
    """Randomizes the letters in the input string."""
    if not input_string:
        return "Input string is empty."

    randomized = ""
    indices = list(range(len(input_string)))
    while indices:
        random_index = random.choice(indices)
        randomized += input_string[random_index]
        indices.remove(random_index)

    return randomized


def find_all_indexes(main_string, sub_string):
    """
    Finds all starting indexes of sub_string within main_string.
    """
    if not sub_string:
        return ""

    indexes = ""
    start = 0
    while True:
        try:
            index = main_string.index(sub_string, start)
            if indexes:
                indexes += ","
            indexes += str(index)
            start = index + 1
        except ValueError:
            break

    return indexes
