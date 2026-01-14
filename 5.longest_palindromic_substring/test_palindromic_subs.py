import unittest
from palindromic_subs import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_character(self):
        self.assertEqual(self.sol.longestPalindrome("a"), "a")

    def test_two_same_characters(self):
        self.assertEqual(self.sol.longestPalindrome("aa"), "aa")

    def test_two_different_characters(self):
        result = self.sol.longestPalindrome("ab")
        self.assertIn(result, ["a", "b"])

    def test_example_babad(self):
        result = self.sol.longestPalindrome("babad")
        self.assertIn(result, ["bab", "aba"])

    def test_example_cbbd(self):
        self.assertEqual(self.sol.longestPalindrome("cbbd"), "bb")

    def test_even_length_palindrome(self):
        self.assertEqual(self.sol.longestPalindrome("abba"), "abba")

    def test_odd_length_palindrome(self):
        self.assertEqual(self.sol.longestPalindrome("racecar"), "racecar")

    def test_palindrome_in_middle(self):
        self.assertEqual(self.sol.longestPalindrome("xyzracecarabc"), "racecar")

    def test_all_same_characters(self):
        self.assertEqual(self.sol.longestPalindrome("aaaaaa"), "aaaaaa")

    def test_multiple_valid_answers(self):
        result = self.sol.longestPalindrome("abacdfgdcaba")
        self.assertIn(result, ["aba"])

    def test_digits_and_letters(self):
        self.assertEqual(self.sol.longestPalindrome("a1b2b1a"), "a1b2b1a")

    def test_no_long_palindrome(self):
        result = self.sol.longestPalindrome("abcdef")
        self.assertIn(result, list("abcdef"))

    def test_long_input(self):
        s = "a" * 1000
        self.assertEqual(self.sol.longestPalindrome(s), s)


if __name__ == "__main__":
    unittest.main()
