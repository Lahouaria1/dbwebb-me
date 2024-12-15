#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
"""

def greet():
    """
    Greet the user and ask for their name.
    """
    name = input("What is your name? ")
    print(f"\nHello {name}, your awesomeness!")

def celsius_to_fahrenheit():
    """
    Convert Celsius to Fahrenheit. Takes input inside the function.
    """
    try:
        celsius = float(input("Enter the temperature in Celsius: "))  # Input inside the function
        fahrenheit = celsius * 9/5 + 32
        print(f"The temperature {celsius}°C is equivalent to {fahrenheit:.2f}°F")
    except ValueError:
        print("Please enter a valid number.")

def points_to_grade():
    """
    Takes user input for max score and user score, calculates the percentage,
    and prints the corresponding grade in the format 'score: <grade>'.
    """
    try:
        # Get input values for max score and user score with prompts
        max_score = float(input("Enter the maximum score: "))  
        user_score = float(input("Enter your score: "))
      
        if max_score <= 0:
            print("Maximum score must be greater than zero.")
            return

        # Calculate the score percentage
        score_percentage = (user_score / max_score) * 100

        # Determine the grade based on the percentage
        if score_percentage >= 90:
            grade = "A"
        elif score_percentage >= 80:
            grade = "B"
        elif score_percentage >= 70:
            grade = "C"
        elif score_percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"score: {grade}")

    except ValueError:
        print("Please enter valid numbers.")

def sum_and_average():
    """
    Prompts the user to enter numbers and calculates their sum and average.
    """
    total_sum = 0
    count = 0

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input == "done":
            break
        try:
            number = float(user_input)
            total_sum = total_sum + number
            count = count + 1
        except ValueError:
            print("Please enter a valid number.")
    
    if count > 0:
        average = total_sum / count
        print(f"The total sum is {total_sum:.2f} and the average is {average:.2f}.")
    else:
        print("No valid numbers were entered.")

def hyphen_string():
    """
    Process the input string to create a new string with repeated characters and hyphens.
    For example, 'abc' would become 'a-bb-ccc' without using join().
    """
    input_string = input("Enter a string to process: ")

    if not input_string:  
        print("Input string is empty.")
        return

    # Process the input string
    result = ""
    for index, char in enumerate(input_string):
        if index > 0:
            result += "-"  # Manually add the hyphen before the next group
        result += char * (index + 1)  # Repeat the character (index + 1) times

    print(f"Processed string: {result}")
    
def compare_numbers():
    """
    Continuously prompts the user to input numbers and compares each input.
    """
    previous_number = None

    while True:
        user_input = input("Skriv ett tal eller 'done': ")

        if user_input.lower() == "done":
            break

        try:
            current_number = int(user_input)  # Convert input to integer

            if previous_number is None:  # Check if it's the first number
                previous_number = current_number
                print("Första talet inmatat. Vänligen ange nästa tal.")
            else:
                # Compare current number with the previous number
                if current_number > previous_number:
                    print("larger!")
                elif current_number < previous_number:
                    print("smaller!")
                else:
                    print("same!")

                # Update previous number
                previous_number = current_number

        except ValueError:
            print("not a number!")

def validate_ssn():
    """Validate a personal identification number (SSN) using the Luhn algorithm."""
    ssn = input("Enter SSN (format: YYMMDD-XXXX or YYYMMDDXXXX): ").replace("-", "")
    
    if len(ssn) != 10:
        print("Not valid.")
        return
    
    total_sum = 0
    for i, digit in enumerate(ssn):
        if not digit.isdigit():
            print("Not valid.")
            return
        
        digit = int(digit)
        if i % 2 == 0:  # If index is even, multiply by 2
            digit *= 2
            if digit > 9:  # If the result is greater than 9, sum the digits
                digit -= 9
        total_sum += digit
    
    if total_sum % 10 == 0:
        print("Valid")
    else:
        print("Not valid")

def robber_language():
    """
    Translates a word into Rövarspråket.
    """
    word = input("Skriv ett ord: ")
    vowels = "AEIOUYÅÄÖaeiouyåäö"
    translated_word = ""

    # Translate into Rövarspråket
    for char in word:
        if char in vowels:
            translated_word =  translated_word + char  # Add vowel as it is
        else:
            translated_word =  translated_word + char + "o" + char  # Add 'o' after the consonant
            
    print(translated_word)
