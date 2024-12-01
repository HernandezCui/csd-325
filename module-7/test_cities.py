import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        """Test the city_country function."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")
        
        result = city_country("lima", "peru")
        self.assertEqual(result, "Lima, Peru")
        
        result = city_country("new york", "usa")
        self.assertEqual(result, "New York, Usa")

if __name__ == '__main__':
    unittest.main()