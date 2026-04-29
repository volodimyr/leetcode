import unittest
from great import Solution


class TestMakeGood(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.makeGood("leEeetcode"), "leetcode")

    def test_example2(self):
        self.assertEqual(self.s.makeGood("abBAcC"), "")

    def test_example3(self):
        self.assertEqual(self.s.makeGood("s"), "s")

    def test_already_good(self):
        self.assertEqual(self.s.makeGood("abc"), "abc")

    def test_single_pair(self):
        self.assertEqual(self.s.makeGood("aA"), "")

    def test_all_same_case(self):
        self.assertEqual(self.s.makeGood("ABCD"), "ABCD")


if __name__ == "__main__":
    unittest.main()
