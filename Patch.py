import unittest
from unittest.mock import patch

from Capital_letters import capitalize_string
class TestCapitalizingStringWithMocks(unittest.TestCase):
    
    @patch('__main__.capitalize_string')
    def test_capitalize_string_called_once(self, mock_capitalize_string):
        mock_capitalize_string.return_value = "HELLO"
        result = capitalize_string("hello")
        mock_capitalize_string.assert_called_once_with("hello")
        self.assertEqual(result, "HELLO")
    
    @patch('__main__.capitalize_string')
    def test_capitalize_string_called_with_uppercase(self, mock_capitalize_string):
        mock_capitalize_string.return_value = "HELLO"
        result = capitalize_string("HELLO")
        mock_capitalize_string.assert_called_once_with("HELLO")
        self.assertEqual(result, "HELLO")
    
    @patch('__main__.capitalize_string')
    def test_capitalize_string_return_value(self, mock_capitalize_string):
        mock_capitalize_string.return_value = "HELLO"
        result = capitalize_string("heLLo")
        self.assertEqual(result, "HELLO")
