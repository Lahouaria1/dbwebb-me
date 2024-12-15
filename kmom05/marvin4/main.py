"""
Main module for interacting with Marvin. 
This module handles user interactions and provides various features related to country data, conversions, 
inventory management, and other Marvin utilities.
"""

import marvin1
import marvin2
import inventory
from inventory import pick, inventory, drop, swap
from marvin2 import get_acronym, randomize_string, find_all_indexes
from emission_functions import get_country_change_for_years, search_country, get_country_data, print_country_data

def main():
    """
    Huvudfunktion för att interagera med användaren och ge olika tjänster genom Marvin.
    """
    marvin_image = r"""
                  .''       
      ._.-.___.' (\      
    //(        ( '
    '/ )\ ).__. ) 
    ' <' \ ._/'\
         \     \
    """
    bag = []  
    stop = False

    while not stop:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do for you?")
        print("Try out my 'inv' commands!")
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
        print("\nTry out my 'inv' commands!")
        print("13) Search for a country.")
        print("14) Calculate emission change between two years.")
        print("15) Show country data.\n")
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
            input_string = input("Enter a string to create an acronym: ")
            acronym = get_acronym(input_string)
            print(f"Acronym: {acronym}")

        elif choice == "11":
            input_string = input("Enter a word to randomize: ")
            randomized_string = randomize_string(input_string)
            print(f"{input_string} --> {randomized_string}")

        elif choice == "12":
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring: ")
            indexes = find_all_indexes(main_string, sub_string)
            print(f"Indexes found: {indexes}")
        
        elif choice == "13":
            search_word = input("Enter part of the country's name: ").strip()
            try:
                matching_countries = search_country(search_word)
                if matching_countries:
                    print("Matching countries:")
                    for country in matching_countries:
                        print(f"- {country}")
                else:
                    print("No countries found.")
            except ValueError as error:
                print(error)


        elif choice == "14":
            input_str = input("Enter country, year1, year2 (e.g., Sweden,1990,2017): ")
            parts = input_str.split(",")
            if len(parts) != 3:
                print("Invalid input! Use format 'country,year1,year2'.")
                continue
            
            country = parts[0].strip()
            try:
                year1 = int(parts[1].strip())
                year2 = int(parts[2].strip())
                change = get_country_change_for_years(country, year1, year2)
                print(f"{country}:{change}%")
            except ValueError as error:
                print(f"Error: {error}")


        elif choice == "15":
            country_name = input("Enter country name: ").strip().capitalize()  
            try:
                data = get_country_data(country_name)
                print_country_data(data)
            except ValueError:
                print(f"Country '{country_name}' not found.")
        elif "inv" in choice:
            print("Inventory commands go here!")

        elif "inv pick" in choice:
            input_item = choice.split()
            if len(input_item) == 3:  
                item = input_item[2]
                pick(bag, item)
            elif len(input_item) == 4:  
                item = input_item[2]
                position = input_item[3]
                pick(bag, item, position)  
            else:
                print("Error: Use 'inv pick <item>' or 'inv pick <item> <position>'")

        elif "inv drop" in choice:
            input_item = choice.split()
            if len(input_item) == 3:
                item = input_item[2]
                drop(bag, item)
            else:
                print("Error: Use 'inv drop <item>'")

        elif "inv swap" in choice:
            input_item = choice.split()
            if len(input_item) == 4:
                item1 = input_item[2]
                item2 = input_item[3]
                swap(bag, item1, item2)
            else:
                print("Error: Use 'inv swap <item1> <item2>'")

        elif choice == "inv":
            inventory(bag)

        else:
            print("That is not a valid choice. Please choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
