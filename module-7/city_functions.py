def city_country(city, country, population=None):
    """Return a city and country in the format 'City, Country - population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
# Testing the function
print(city_country("santiago", "chile", 5000000))
print(city_country("lima", "peru"))
print(city_country("new york", "usa", 8419600))