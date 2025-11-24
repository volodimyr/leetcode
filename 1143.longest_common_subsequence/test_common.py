import unittest
from common import Solution

class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("abcde", "ace"),
            3
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("abc", "abc"),
            3
        )

    def test_example3(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("abc", "def"),
            0
        )

    def test_single_char_match(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("a", "a"),
            1
        )

    def test_single_char_no_match(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("a", "b"),
            0
        )

    def test_repeated_characters(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("aaaaa", "aa"),
            2
        )

    def test_interleaved(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("axbycz", "abc"),
            3
        )

    def test_no_overlap(self):
        self.assertEqual(
            self.sol.longestCommonSubsequence("xyz", "abc"),
            0
        )

    def test_large_strings(self):
        # LCS is the whole string
        s1 = "a" * 500
        s2 = "a" * 500
        self.assertEqual(
            self.sol.longestCommonSubsequence(s1, s2),
            500
        )

    def test_large_strings_partial(self):
        s1 = "a" * 300 + "b" * 300
        s2 = "a" * 500
        self.assertEqual(
            self.sol.longestCommonSubsequence(s1, s2),
            300
        )


if __name__ == "__main__":
    unittest.main()
