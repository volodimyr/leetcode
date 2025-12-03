import unittest
from substring import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Input: s = "babad"
        # Output: "bab" or "aba"
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])
        self.assertEqual(len(result), 3)

    def test_example_2(self):
        # Input: s = "cbbd"
        # Output: "bb"
        s = "cbbd"
        self.assertEqual(self.solution.longestPalindrome(s), "bb")

    def test_single_character(self):
        # Constraint: 1 <= s.length
        s = "a"
        self.assertEqual(self.solution.longestPalindrome(s), "a")

    def test_all_same_characters(self):
        s = "aaaaa"
        self.assertEqual(self.solution.longestPalindrome(s), "aaaaa")

    def test_no_palindrome_longer_than_one(self):
        s = "abcde"
        self.assertEqual(self.solution.longestPalindrome(s), "a") # or "b", "c", "d", "e"

    def test_long_complex_string(self):
        s = "bananas"
        # Longest palindrome is "anana" (length 5)
        self.assertEqual(self.solution.longestPalindrome(s), "anana")

    def test_palindrome_at_start(self):
        s = "racecarxyz"
        self.assertEqual(self.solution.longestPalindrome(s), "racecar")

    def test_palindrome_at_end(self):
        s = "xyzracecar"
        self.assertEqual(self.solution.longestPalindrome(s), "racecar")

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)