#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesn't do anything, just presents a menu with some choices.
You should add functionality to Marvin.
"""

marvin_image = r"""
              .''       
  ._.-.___.' (`\      
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\
   `   \     \
"""

# Function for converting temperature from Celsius to Fahrenheit (Menu option 2)
def celsius_to_fahrenheit(temp_celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return temp_celsius * 9 / 5 + 32

# Function for converting score percentage to grade 
def calculate_grade(score_percentage):
    """Convert score percentage to a grade based on the given scale."""
    if score_percentage >= 90:
        return "A"
    if score_percentage >= 80:
        return "B"
    if score_percentage >= 70:
        return "C"
    if score_percentage >= 60:
        return "D"
    return "F"  

# Function to process the input string 
def process_string(input_string):
    """
    Process the input string to create a new string with repeated characters.
    """
    result = []
    for index, char in enumerate(input_string):  # Using enumerate
        result.append(char * (index + 1))  # Repeat the character
    return '-'.join(result)

# Function to compare numbers 
def compare_numbers():
    """
    Continuously ask the user for numbers and compare them.
    """
    previous_number = None
    
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")  # Variable renamed
        
        if user_input.lower() == 'done':
            break
        
        try:
            current_number = float(user_input)
            
            if previous_number is None:
                previous_number = current_number
                print("First number saved. Please enter another number.")
                continue
            
            # Compare current number with previous number
            if current_number > previous_number:
                print("larger!")
            elif current_number < previous_number:
                print("smaller!")
            else:
                print("same!")
            
            previous_number = current_number
        
        except ValueError:
            print("not a number!")

# Function to validate Swedish personal number using Luhn algorithm
def validate_personnummer(pnr):
    """
    Validate a Swedish personal number using the Luhn algorithm.
    """
    pnr = pnr.replace("-", "")
    if len(pnr) not in [10, 12] or not pnr.isdigit():
        return "Not valid"
    
    digits = [int(d) for d in pnr]
    total_sum = 0

    for index, digit in enumerate(digits):  
        if (len(digits) - index) % 2 == 0:  
            doubled_value = digit * 2
            total_sum += (doubled_value - 9) if doubled_value > 9 else doubled_value
        else:
            total_sum += digit

    return "Valid" if total_sum % 10 == 0 else "Not valid"

# Function to translate to Rövarspråket
def to_rovarspraket(word_input):
    """Translate a word to Rövarspråket."""
    vowels = "AEIOUYÅÄÖaeiouyåäö"
    translated = ""
    
    for char in word_input:
        if char in vowels:
            translated += char  # Vowels remain unchanged
        else:
            translated += char + 'o' + char  # Consonants get the "o" insertion
            
    return translated

# Main loop
stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")
    print("1) Present yourself to Marvin.")
    print("2) Convert Celsius to Fahrenheit.")
    print("3) Convert points to a grade.")
    print("4) How long have you been working?")
    print("5) Process a string.")
    print("6) Compare numbers.")
    print("7) Validate a personal number.")
    print("8) Translate to Rövarspråket.")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        stop = True

    elif choice == "1":
        name = input("What is your name? ")
        print(f"\nMarvin says:\nHello {name} - your awesomeness!")
    
    elif choice == "2":
        try:
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"The temperature {celsius}°C is equivalent to {fahrenheit:.2f}°F.")
        except ValueError:
            print("Please enter a valid number for the temperature.")

    elif choice == "3":
        try:
            max_score = float(input("Enter the maximum possible score: "))
            user_score = float(input("Enter your score: "))

            if max_score <= 0:
                print("Maximum score must be greater than zero.")
            else:
                score_pct = (user_score / max_score) * 100
                grade = calculate_grade(score_pct)
                print(f"score: {grade}")
        except ValueError:
            print("Please enter valid numbers for the scores.")

    elif choice == "4":
        numbers = []  # List to hold user inputs
        while True:
            current_input = input("Enter a number (or type 'done' to finish): ")
            if current_input.lower() == 'done':
                break
            
            try:
                number = float(current_input)
                numbers.append(number)
            except ValueError:
                print("Please enter a valid number.")
        
        if numbers:
            total = sum(numbers)
            average = total / len(numbers)
            print(f"The sum of all numbers is {total:.2f} and the average is {average:.2f}.")
        else:
            print("No valid numbers were entered.")

    elif choice == "5":
        string_input = input("Enter a string: ") 
        processed_string = process_string(string_input)
        print(f"Processed string: {processed_string}")

    elif choice == "6":
        compare_numbers()

    elif choice == "7":
        personal_number = input("Enter a personal number: ")
        validation_result = validate_personnummer(personal_number)
        print(validation_result)  

    elif choice == "8":
        input_word = input("Enter a word: ")
        translated_word = to_rovarspraket(input_word)
        print(f"Translated to Rövarspråket: {translated_word}")

    if not stop:
        input("\nPress enter to continue...")
        