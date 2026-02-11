import unittest
from min import Solution


class TestMinWindow(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # Basic example from LeetCode
    def test_example_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(self.sol.minWindow(s, t), "BANC")

    # Single character exact match
    def test_single_char(self):
        s = "a"
        t = "a"
        self.assertEqual(self.sol.minWindow(s, t), "a")

    # No possible window
    def test_no_match(self):
        s = "a"
        t = "aa"
        self.assertEqual(self.sol.minWindow(s, t), "")

    # Entire string is the window
    def test_full_string(self):
        s = "ABC"
        t = "ABC"
        self.assertEqual(self.sol.minWindow(s, t), "ABC")

    # Multiple possible windows, ensure smallest returned
    def test_multiple_windows(self):
        s = "aaabdabcefaecbef"
        t = "abc"
        self.assertEqual(self.sol.minWindow(s, t), "abc")

    # Case sensitivity test
    def test_case_sensitive(self):
        s = "aAbBcC"
        t = "ABC"
        self.assertEqual(self.sol.minWindow(s, t), "AbBcC")

    # Repeated characters in t
    def test_repeated_characters(self):
        s = "AAABBC"
        t = "AABC"
        self.assertEqual(self.sol.minWindow(s, t), "AABBC")

    # Empty t
    def test_empty_t(self):
        s = "ABC"
        t = ""
        self.assertEqual(self.sol.minWindow(s, t), "")

    # Empty s
    def test_empty_s(self):
        s = ""
        t = "ABC"
        self.assertEqual(self.sol.minWindow(s, t), "")


if __name__ == "__main__":
    unittest.main()
