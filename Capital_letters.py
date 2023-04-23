import unittest

class TestCapitalizingString(unittest.TestCase):
    def test_capitalize_all_lower_case(self):
        self.assertEqual(capitalize_string("hello"), "HELLO")
    
    def test_capitalize_all_upper_case(self):
        self.assertEqual(capitalize_string("HELLO"), "HELLO")
    
    def test_capitalize_mixed_case(self):
        self.assertEqual(capitalize_string("heLLo"), "HELLO")
    
    def test_capitalize_with_numbers(self):
        self.assertEqual(capitalize_string("he1Lo"), "HE1LO")
    
    def test_capitalize_with_special_characters(self):
        self.assertEqual(capitalize_string("he#lLo"), "HE#LLO")
def capitalize_string(string):
    return string.upper()
