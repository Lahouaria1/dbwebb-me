"""
This module contains functions for calculating and retrieving emission data 
for various countries, including emissions from the years 1990, 2005, and 2017.
"""

import emission_data

def search_country(search_word):
    """
    Search for countries in the emission data based on a search word.
    Returns a list of countries that match the search.
    """
    search_word = search_word.lower()  
    result = [] 
  
    for country in emission_data.country_data:
  
        if search_word in country.lower():
            result.append(country)  

    # If no country matches, raise an error
    if not result:
        raise ValueError("Country does not exist!")

    return result 

def get_country_year_data_megaton(country, year):
    """
    Returns the emission data of a country for a specific year in tons.
    """
    # A dictionary to map years to the corresponding emission data
    year_map = {
        1990: emission_data.emission_1990,
        2005: emission_data.emission_2005,
        2017: emission_data.emission_2017
    }

    # Check if the given year is valid
    if year not in year_map:
        raise ValueError("Wrong year!")

    country = country.strip().title()

    for key, value in emission_data.country_data.items():
        if key.lower() == country.lower():  
            country_id = value['id']  
          
            return year_map[year].get(country_id, 0) * 1_000_000  # Convert to tons

    # If country is not found in the data, raise an error
    raise ValueError(f"Country '{country}' not found in data.")

def get_country_change_for_years(country, year1, year2):
    """
    Calculates the percent change in emissions for a country between two years.
    Uses get_country_year_data_megaton to fetch emission data.
    """

    data_year1 = get_country_year_data_megaton(country, year1)
    data_year2 = get_country_year_data_megaton(country, year2)

    if data_year1 == 0:
        return 0

    # Calculate the percentage change in emissions
    change = ((data_year2 - data_year1) / data_year1) * 100
    return round(change, 2)  # Round to two decimal places


def get_country_data(country_name):
    """
    Retrieves all data for a specific country and returns a structured dictionary.
    Raises ValueError if the country does not exist.
    """
    # Check if the country exists in the data
    if country_name not in emission_data.country_data:
        raise ValueError("Country does not exist!")

    # Get country information from the data
    country_info = emission_data.country_data[country_name]
    population_data = country_info.get("population", None)  

    # Create a dictionary to store all the relevant data
    data = {
        'name': country_name,
        1990: {
            'emission': get_country_year_data_megaton(country_name, 1990),
            'population': population_data[0] if population_data else None
        },
        2005: {
            'emission': get_country_year_data_megaton(country_name, 2005),
            'population': population_data[1] if population_data else None
        },
        2017: {
            'emission': get_country_year_data_megaton(country_name, 2017),
            'population': population_data[2] if population_data else None
        },
        'emission_change': (
            get_country_change_for_years(country_name, 1990, 2005),
            get_country_change_for_years(country_name, 2005, 2017)
        )
    }

    return data 

def print_country_data(data):
    """
    Prints formatted country data.
    """
    name = data['name']
    change = data['emission_change']
    print(name)
    print(f"Emission-1990: {data[1990]['emission']} 2005: {data[2005]['emission']} 2017: {data[2017]['emission']}")
    print(f"Emission change -1990-2005: {change[0]}% 2005-2017: {change[1]}%")

    # Print population data for each year if available
    for year in [1990, 2005, 2017]:
        population = data[year]['population']
        if population is not None:
            print(f"Population- {year}: {population}")
        else:
            print(f"Population- {year}: Missing population data!")
