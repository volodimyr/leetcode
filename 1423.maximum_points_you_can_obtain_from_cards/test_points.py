import unittest
from typing import List
from points import Solution


class TestMaxScore(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12)

    def test_example2(self):
        self.assertEqual(self.s.maxScore([2, 2, 2], 2), 4)

    def test_example3(self):
        self.assertEqual(self.s.maxScore([9, 7, 7, 9, 7, 7, 9], 7), 55)

    def test_k_equals_1(self):
        self.assertEqual(self.s.maxScore([1, 79, 80, 1, 1, 1, 200, 1], 1), 1)

    def test_take_all(self):
        self.assertEqual(self.s.maxScore([5, 5, 5], 3), 15)

    def test_single_card(self):
        self.assertEqual(self.s.maxScore([100], 1), 100)


if __name__ == "__main__":
    unittest.main()
