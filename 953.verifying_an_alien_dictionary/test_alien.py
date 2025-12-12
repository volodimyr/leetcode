import unittest

from typing import List
from alien import Solution

class TestAlienDictionary(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_example_2(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_example_3(self):
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_single_word(self):
        words = ["abc"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_identical_words(self):
        words = ["z", "z", "z"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_prefix_but_correct_order(self):
        words = ["app", "apple"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_unsorted_due_to_middle_char(self):
        words = ["ab", "aa"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.s.isAlienSorted(words, order))

    def test_custom_order(self):
        words = ["baa", "abcd", "abca", "cab", "cad"]
        order = "bdefghijklmnopqrstuvwxzayc"
        # Order where 'b' < 'a' < 'c'
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test_large_input(self):
        words = ["a"] * 100
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))


if __name__ == "__main__":
    unittest.main()
