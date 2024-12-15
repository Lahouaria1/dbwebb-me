#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main.py
"""
Marvin with a simple menu to start up with.
Marvin presents a menu with some choices and does simple tasks.
"""

import marvin1
import marvin2
from marvin2 import get_acronym, randomize_string, find_all_indexes
# Import specific functions from marvin2

def main():
    """
    Main function to interact with the user and provide various services through Marvin.
    """
    marvin_image = r"""
                  .''       
      ._.-.___.' (`\      
    //(        ( `'
    '/ )\ ).__. ) 
    ' <' `\ ._/'\
      `   \     \
    """
    
    stop = False
    while not stop:
        # Clear the screen and present the menu
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Convert Celsius to Fahrenheit.")
        print("3) Convert points to a grade.")
        print("4) Calculate sum and average.")
        print("5) Hyphen string.")
        print("6) Compare numbers.")
        print("7) Validate personal identification number (SSN).")
        print("8) Translate to Rövarspråket.")
        print("9) Create personal identification number (SSN).")
        print("10) Get acronym from a string.")
        print("11) Randomize a string.")
        print("12) Find all indexes of a substring.")
        print("q) Quit.")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "1":
            marvin1.greet()

        elif choice == "2":
            marvin1.celsius_to_fahrenheit()

        elif choice == "3":
            marvin1.points_to_grade() 

        elif choice == "4":
            marvin1.sum_and_average()

        elif choice == "5":
            marvin1.hyphen_string()
            
        elif choice == "6":  
            marvin1.compare_numbers()
            
        elif choice == "7":  
            marvin1.validate_ssn()

        elif choice == "8":  
            marvin1.robber_language()

        elif choice == "9":  
            birth_date = input("Enter birth date (YYMMDD): ")
            print(marvin2.create_ssn(birth_date))
        elif choice == "10":
            input_string = input("Skriv in en sträng för att skapa en akronym: ")
            acronym = get_acronym(input_string)
            print(f"Akronym: {acronym}")
        elif choice == "11":
            input_string = input("Enter a word to randomize: ")
            randomized_string = randomize_string(input_string)
            print(f"{input_string} --> {randomized_string}")

        elif choice == "12":
            main_string = input("Skriv in huvudsträngen: ")
            sub_string = input("Skriv in substringen: ")
            indexes = find_all_indexes(main_string, sub_string)
            print(f"Index hittade: {indexes}")
        else:
            print("That is not a valid choice. Please choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
    