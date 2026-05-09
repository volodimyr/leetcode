import unittest
from find import Solution

class TestNumKLenSubstrNoRepeats(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("havefunonneetcode", 5), 6)

    def test_example2(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("home", 5), 0)

    def test_k_equals_length(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("abcd", 4), 1)

    def test_all_same_chars(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("aaaa", 2), 0)

    def test_k_equals_one(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("abc", 1), 3)

    def test_single_char_string(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("a", 1), 1)

    def test_no_valid_substrings(self):
        self.assertEqual(self.solution.numKLenSubstrNoRepeats("aab", 2), 1)

if __name__ == "__main__":
    unittest.main()
