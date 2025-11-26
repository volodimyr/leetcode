import unittest
from typing import List
from spaces import Solution

class TestAddSpaces(unittest.TestCase):
    
    def setUp(self):
        """Initialize the solution instance before each test."""
        self.solution = Solution()

    def test_example_1_multiple_spaces(self):
        """Test standard case with multiple insertions."""
        s = "LeetcodeHelpsMeLearn"
        spaces = [8, 13, 15]
        expected = "Leetcode Helps Me Learn"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_example_2_short_words(self):
        """Test case resulting in short words and multiple adjacent spaces."""
        s = "icodeinpython"
        spaces = [1, 5, 7, 9]
        expected = "i code in py thon"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_example_3_space_at_start(self):
        """Test case where a space is inserted before the first character (index 0)."""
        s = "spacing"
        spaces = [0, 1, 2, 3, 4, 5, 6]
        expected = " s p a c i n g"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)
        
    def test_no_spaces(self):
        """Test edge case where spaces list is empty."""
        s = "NoSpacesHere"
        spaces = []
        expected = "NoSpacesHere"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_space_at_end_of_string(self):
        """Test placing a space just before the last character (max valid index)."""
        s = "EndOfWord" # Length 9, indices 0-8
        spaces = [8]
        expected = "EndOfWor d"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

    def test_mixed_case(self):
        """Test with a mix of uppercase and lowercase letters."""
        s = "CamelCaseString"
        spaces = [5, 9]
        expected = "Camel Case String"
        self.assertEqual(self.solution.addSpaces(s, spaces), expected)

if __name__ == '__main__':
    unittest.main()