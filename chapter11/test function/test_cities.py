import unittest
from city_functions import get_city_country

class NameTest(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_city_country('santos', 'brazil')
        self.assertEqual(formatted_name,'Santos, Brazil')
    
    def test_city_country_population(self):
        formatted_name = get_city_country('santos','brazil', 5000000)
        self.assertEqual(formatted_name,'Santos, Brazil - Population 5000000')

if __name__ == '__main__':
    unittest.main()
    