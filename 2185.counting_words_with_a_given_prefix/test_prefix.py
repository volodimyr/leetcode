import unittest
from prefix import Solution

class TestPrefixCount(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        words = ["pay", "attention", "practice", "attend"]
        pref = "at"
        self.assertEqual(self.sol.prefixCount(words, pref), 2)

    def test_example2(self):
        words = ["leetcode", "win", "loops", "success"]
        pref = "code"
        self.assertEqual(self.sol.prefixCount(words, pref), 0)

    def test_single_match(self):
        words = ["apple", "apricot", "banana"]
        pref = "app"
        self.assertEqual(self.sol.prefixCount(words, pref), 1)

    def test_all_match(self):
        words = ["a", "ab", "abc", "abcd"]
        pref = "a"
        self.assertEqual(self.sol.prefixCount(words, pref), 4)

    def test_no_match(self):
        words = ["cat", "dog", "fish"]
        pref = "z"
        self.assertEqual(self.sol.prefixCount(words, pref), 0)

    def test_prefix_longer_than_words(self):
        words = ["hi", "hello"]
        pref = "hello!"
        self.assertEqual(self.sol.prefixCount(words, pref), 0)

    def test_duplicate_words(self):
        words = ["at", "at", "attention"]
        pref = "at"
        self.assertEqual(self.sol.prefixCount(words, pref), 3)

    def test_empty_list(self):
        words = []
        pref = "any"
        self.assertEqual(self.sol.prefixCount(words, pref), 0)

    def test_single_letter_prefix(self):
        words = ["x", "xy", "xyz", "yy"]
        pref = "x"
        self.assertEqual(self.sol.prefixCount(words, pref), 3)


if __name__ == "__main__":
    unittest.main()
