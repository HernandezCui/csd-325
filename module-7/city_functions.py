def city_country(city, country, population=None, language=None):
    """Return a city and country in the format 'City, Country - population xxx, Language'."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    elif language:
        return f"{city.title()}, {country.title()}, {language.title()}"
    else:
        return f"{city.title()}, {country.title()}"
    
# Testing the function
print(city_country("santiago", "chile", 5000000, "spanish"))
print(city_country("lima", "peru", language="spanish"))
print(city_country("new york", "usa", 8419600, "english"))