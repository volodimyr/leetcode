import unittest
from typing import List

numbers_map = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
}

from phone_number import Solution

class TestLetterCombinations(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example1_two_digits(self):
        """Test with digits '23' - basic two digit case"""
        result = self.solution.letterCombinations("23")
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 9)  # 3 * 3 = 9 combinations
    
    def test_example2_single_digit(self):
        """Test with single digit '2'"""
        result = self.solution.letterCombinations("2")
        expected = ["a","b","c"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_empty_string(self):
        """Test with empty string - should return empty list"""
        result = self.solution.letterCombinations("")
        self.assertEqual(result, [])
    
    def test_single_digit_various(self):
        """Test various single digits"""
        # Digit 7 has 4 letters
        result = self.solution.letterCombinations("7")
        expected = ["p","q","r","s"]
        self.assertEqual(sorted(result), sorted(expected))
        
        # Digit 9 has 4 letters
        result = self.solution.letterCombinations("9")
        expected = ["w","x","y","z"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_three_digits(self):
        """Test with three digits"""
        result = self.solution.letterCombinations("234")
        # 2 has 3 letters, 3 has 3 letters, 4 has 3 letters = 27 combinations
        self.assertEqual(len(result), 27)
        # Check a few specific combinations
        self.assertIn("adg", result)
        self.assertIn("beh", result)
        self.assertIn("cfi", result)
    
    def test_four_digits_max_length(self):
        """Test with four digits (maximum constraint)"""
        result = self.solution.letterCombinations("2345")
        # 3 * 3 * 3 * 3 = 81 combinations
        self.assertEqual(len(result), 81)
        # Check first and last combinations (alphabetically)
        self.assertIn("adgj", result)
        self.assertIn("cfil", result)
    
    def test_digits_with_seven_and_nine(self):
        """Test with digits 7 and 9 which have 4 letters each"""
        result = self.solution.letterCombinations("79")
        # 4 * 4 = 16 combinations
        self.assertEqual(len(result), 16)
        self.assertIn("pw", result)
        self.assertIn("sz", result)
        self.assertIn("qx", result)
    
    def test_all_same_digit(self):
        """Test with repeating same digit"""
        result = self.solution.letterCombinations("222")
        # 3 * 3 * 3 = 27 combinations
        self.assertEqual(len(result), 27)
        self.assertIn("aaa", result)
        self.assertIn("abc", result)
        self.assertIn("ccc", result)
    
    def test_no_duplicates(self):
        """Ensure no duplicate combinations in result"""
        result = self.solution.letterCombinations("23")
        self.assertEqual(len(result), len(set(result)))
    
    def test_all_combinations_correct_length(self):
        """Verify all combinations have correct length"""
        digits = "234"
        result = self.solution.letterCombinations(digits)
        for combo in result:
            self.assertEqual(len(combo), len(digits))
    
    def test_digit_range_2_to_9(self):
        """Test all digits from 2 to 9"""
        for digit in "23456789":
            result = self.solution.letterCombinations(digit)
            self.assertGreater(len(result), 0)
            expected_len = len(numbers_map[digit])
            self.assertEqual(len(result), expected_len)
    
    def test_order_independence(self):
        """Test that results contain all expected combinations regardless of order"""
        result = self.solution.letterCombinations("23")
        # Manually check all 9 combinations exist
        expected_combos = []
        for c1 in "abc":
            for c2 in "def":
                expected_combos.append(c1 + c2)
        
        self.assertEqual(sorted(result), sorted(expected_combos))


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)