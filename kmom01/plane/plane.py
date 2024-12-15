#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
str1 = "Hello World in a variable"
print(str1)

# Combine two strings and print them out
str2 = "Hello World!"
str3 = "Its a nice day today!"
print(str2 + " " + str3)

# Combine string and values
a = 40
b = 2
c = a + b
str4 = "Summan är " + str(c) + "."
print(str2 + " " + str4)
    # Funktion för att konvertera hastighet från meter till feet
def meter_to_feet(meter):
    """
    Convert meters to feet.
    
    Args:
        meter (float): The value in meters to be converted.
    
    Returns:
        float: The value converted to feet.
    """
    return meter * 3.28084


    # Funktion för att konvertera hastighet från km/h till mph
def kmh_to_mph(kmh):
    """
    Convert speed from kilometers per hour (km/h) to miles per hour (mph).
    
    Args:
        kmh (float): Speed in kilometers per hour.
    
    Returns:
        float: Speed in miles per hour.
    """
    return kmh * 0.62137

# Funktion för att konvertera temperatur från Celsius till Fahrenheit

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
    
    Returns:
        float: Temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32

# Be användaren mata in höjd, hastighet och temperatur
hojd_meter = float(input("Ange höjd över havet (i meter): "))
hastighet_kmh = float(input("Ange hastighet (i km/h): "))
temperatur_celsius = float(input("Ange temperatur utanför flygplanet (i Celsius): "))

# Konvertera värdena
hojd_feet = meter_to_feet(hojd_meter)
hastighet_mph = kmh_to_mph(hastighet_kmh)
temperatur_fahrenheit = celsius_to_fahrenheit(temperatur_celsius)

# Skriv ut de konverterade värdena
print("\nKonverterade värden:")
print(f"Höjd över havet: {hojd_feet:.2f} feet")
print(f"Hastighet: {hastighet_mph:.2f} mph")
print(f"Temperatur utanför flygplanet: {temperatur_fahrenheit:.2f} °F")
