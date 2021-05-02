import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('helmuth','netto', 'müller')
        self.assertEqual(formatted_name,'Helmuth Müller Netto')

if __name__ == '__main__':
    unittest.main()