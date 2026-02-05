import unittest
from ransom import Solution


class TestRansomNote(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_char_false(self):
        self.assertFalse(self.solution.canConstruct("a", "b"))

    def test_repeated_char_false(self):
        self.assertFalse(self.solution.canConstruct("aa", "ab"))

    def test_repeated_char_true(self):
        self.assertTrue(self.solution.canConstruct("aa", "aab"))

    def test_exact_match(self):
        self.assertTrue(self.solution.canConstruct("abc", "abc"))

    def test_magazine_larger(self):
        self.assertTrue(self.solution.canConstruct("abc", "aabbcc"))

    def test_insufficient_letters(self):
        self.assertFalse(self.solution.canConstruct("aabbc", "aabc"))

    def test_long_strings(self):
        ransom = "a" * 100000
        magazine = "a" * 100000
        self.assertTrue(self.solution.canConstruct(ransom, magazine))

    def test_order_does_not_matter(self):
        self.assertTrue(self.solution.canConstruct("cba", "abc"))


if __name__ == "__main__":
    unittest.main()
