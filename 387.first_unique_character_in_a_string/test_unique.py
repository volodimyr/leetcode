import unittest
from unique import Solution


class TestFirstUniqueCharacter(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.firstUniqChar("leetcode"), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.firstUniqChar("loveleetcode"), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.firstUniqChar("aabb"), -1)

    def test_single_character(self):
        self.assertEqual(self.solution.firstUniqChar("a"), 0)

    def test_all_unique(self):
        self.assertEqual(self.solution.firstUniqChar("abc"), 0)

    def test_unique_in_middle(self):
        self.assertEqual(self.solution.firstUniqChar("aabbcdd"), 4)

    def test_unique_at_end(self):
        self.assertEqual(self.solution.firstUniqChar("aabbccz"), 6)

    def test_long_string(self):
        s = "a" * 100000
        self.assertEqual(self.solution.firstUniqChar(s), -1)


if __name__ == "__main__":
    unittest.main()
