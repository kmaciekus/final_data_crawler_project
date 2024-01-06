import unittest
from final_data_crawler_project.utils.error_handler import text_value_error_handler

class TextValueErrorHandlerTest(unittest.TestCase):

    def test_text_value_error_handler_valid_input(self):
        # Test with valid input
        result = text_value_error_handler("Hello, world!")
        self.assertEqual(result, "Hello, world!")

    def test_text_value_error_handler_empty_input(self):
        # Test with empty input
        result = text_value_error_handler("")
        self.assertEqual(result, "")

    def test_text_value_error_handler_none_input(self):
        # Test with None input
        result = text_value_error_handler(None)
        self.assertEqual(result, "")

    def test_text_value_error_handler_invalid_type(self):
        # Test with invalid input type
        with self.assertRaises(ValueError) as context:
            text_value_error_handler(123)
        self.assertEqual(str(context.exception), "Search text must be string")

    def test_text_value_error_handler_numeric_input(self):
        # Test with numeric input
        with self.assertRaises(ValueError) as context:
            text_value_error_handler("123")
        self.assertEqual(str(context.exception), "Search text must not contain only numbers")

if __name__ == '__main__':
    unittest.main()
