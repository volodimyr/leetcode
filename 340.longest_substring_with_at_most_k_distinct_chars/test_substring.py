import unittest
from substring import Solution

class TestLongestSubstringKDistinct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("eceba", 2), 3)

    def test_example2(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("aa", 1), 2)

    def test_k_zero(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("abc", 0), 0)

    def test_single_char_string(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("a", 1), 1)

    def test_k_greater_than_distinct(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("abc", 10), 3)

    def test_all_same_char(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("aaaaa", 1), 5)

    def test_no_repeating_chars(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("abcdef", 2), 2)

    def test_mixed(self):
        self.assertEqual(self.sol.lengthOfLongestSubstringKDistinct("aabbcc", 2), 4)  # "aabb" or "bbcc"

if __name__ == "__main__":
    unittest.main()
