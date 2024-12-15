#!/usr/bin/env python3
"""
Programmet skriver ut en hälsning till Jack Black
"""
print("Hej Jack Black, du är 48 år gammal.")


"""
Programmet skriver ut en hälsning till Jack Black
"""
input()
print("Hej Jack Black, du är 48 år gammal.") # Skriver ut ett sträng värde

"""
Programmet skriver ut en hälsning till Jack Black
"""

input("Skriv något, klicka sen enter: ")
print("Hej Jack Black, du är 48 år gammal.") # Skriver ut ett sträng värde

"""
Programmet skriver ut en hälsning till Jack Black
"""

name = input("Skriv ett namn, klicka sen enter: ") # Ber användaren mata in ett namn
greeting = "Hej " + name + ", du är 48 år gammal." # Sätter ihop "Hej", name och ", du är 48 år gammal." till ett värde.
print(greeting) # Skriver ut ett sträng värde

greeting = "test" + "24" # Testar konkaternera en sträng med ett heltal bara för att se vad som händer.
year = 2018 # Hårdkodat värde för vilket år det är

name = input("Skriv ett namn, klicka sen enter: ")
age = input("Skriv en ålder, klicka sen enter: ")

year_born = str(year - int(age)) # Födelseår räknas ut. Gör om age från string till integer med int()

greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + year_born
print(greeting)
