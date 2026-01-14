import unittest
from palindromic_subs import Solution


class TestPalindromicSubstrings(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_character(self):
        self.assertEqual(self.sol.countSubstrings("a"), 1)

    def test_example_abc(self):
        self.assertEqual(self.sol.countSubstrings("abc"), 3)

    def test_example_aaa(self):
        self.assertEqual(self.sol.countSubstrings("aaa"), 6)

    def test_two_same_characters(self):
        self.assertEqual(self.sol.countSubstrings("aa"), 3)  # "a", "a", "aa"

    def test_two_different_characters(self):
        self.assertEqual(self.sol.countSubstrings("ab"), 2)  # "a", "b"

    def test_palindrome_center(self):
        self.assertEqual(self.sol.countSubstrings("aba"), 4)  # "a","b","a","aba"

    def test_longer_palindrome(self):
        self.assertEqual(self.sol.countSubstrings("racecar"), 10)

    def test_all_same_characters(self):
        self.assertEqual(self.sol.countSubstrings("aaaa"), 10)

    def test_no_repeated_characters(self):
        self.assertEqual(self.sol.countSubstrings("abcd"), 4)

    def test_mixed_palindromes(self):
        self.assertEqual(self.sol.countSubstrings("aabaa"), 9)


if __name__ == "__main__":
    unittest.main()
