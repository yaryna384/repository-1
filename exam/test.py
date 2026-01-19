# test.py
import unittest
from main import remove_spaces

class TestStringMethods(unittest.TestCase):

    def test_remove_spaces(self):
        # Перевіряємо рядок з пробілами на початку, в кінці та всередині
        test_string = "  Hello World  "
        expected = "HelloWorld"
        
        self.assertEqual(remove_spaces(test_string), expected)

if __name__ == "__main__":
    unittest.main()