import unittest
from final_data_crawler_project.utils.converters import convert_to_float, convert_to_int

class ConversionFunctionsTest(unittest.TestCase):

    def test_convert_to_float_valid_input(self):
        # Test with valid input
        result = convert_to_float("123.45")
        self.assertEqual(result, 123.45)

    def test_convert_to_float_empty_input(self):
        # Test with empty input
        result = convert_to_float("")
        self.assertIsNone(result)

    def test_convert_to_float_invalid_input(self):
        # Test with invalid input
        result = convert_to_float("abc")
        self.assertIsNone(result)

    def test_convert_to_int_valid_input(self):
        # Test with valid input
        result = convert_to_int("123")
        self.assertEqual(result, 123)

    def test_convert_to_int_empty_input(self):
        # Test with empty input
        result = convert_to_int("")
        self.assertIsNone(result)

    def test_convert_to_int_invalid_input(self):
        # Test with invalid input
        result = convert_to_int("abc")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()