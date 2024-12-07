import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        """Test the city_country function."""
        result = city_country("santiago", "chile", 5000000, "spanish")
        self.assertEqual(result, "Santiago, Chile - population 5000000, Spanish")
        
        result = city_country("lima", "peru", language="spanish")
        self.assertEqual(result, "Lima, Peru, Spanish")
        
        result = city_country("new york", "usa", 8419600, "english")
        self.assertEqual(result, "New York, Usa - population 8419600, English")

if __name__ == '__main__':
    unittest.main()