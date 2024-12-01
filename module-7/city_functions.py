def city_country(city, country):
    """Return a city and country in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"
    
# Testing the function
print(city_country("santiago", "chile"))
print(city_country("lima", "peru"))
print(city_country("new york", "usa"))