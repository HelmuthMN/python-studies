import unittest
from salary import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee('Helmuth', 'Muller')
    
    def test_give_default_raise(self):
        final_message = self.employee1.give_raise()
        self.assertEqual(final_message,'The new salary of Helmuth Muller is 5000')

    def test_give_custom_raise(self):
        final_message = self.employee1.give_raise(2000)
        self.assertEqual(final_message, 'The new salary of Helmuth Muller is 7000')  

if __name__ == '__main__':
    unittest.main()