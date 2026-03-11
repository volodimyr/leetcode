import unittest

from index import Solution

class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.strStr("sadbutsad", "sad"), 0)

    def test_example2(self):
        self.assertEqual(self.s.strStr("leetcode", "leeto"), -1)

    def test_needle_at_end(self):
        self.assertEqual(self.s.strStr("sadbutsad", "sad"), 0)
        self.assertEqual(self.s.strStr("butsad", "sad"), 3)

    def test_needle_equals_haystack(self):
        self.assertEqual(self.s.strStr("abc", "abc"), 0)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.s.strStr("ab", "abc"), -1)

    def test_single_char_found(self):
        self.assertEqual(self.s.strStr("a", "a"), 0)

    def test_single_char_not_found(self):
        self.assertEqual(self.s.strStr("a", "b"), -1)

    def test_needle_at_middle(self):
        self.assertEqual(self.s.strStr("hello", "ll"), 2)

    def test_repeated_chars(self):
        self.assertEqual(self.s.strStr("aaa", "aa"), 0)

    def test_no_match(self):
        self.assertEqual(self.s.strStr("mississippi", "pi"), 9)

if __name__ == "__main__":
    unittest.main()
