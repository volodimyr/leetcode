import unittest
from stone import Solution


class TestLastStoneWeightII(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.lastStoneWeightII([2, 7, 4, 1, 8, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.s.lastStoneWeightII([31, 26, 33, 21, 40]), 5)

    def test_single_stone(self):
        self.assertEqual(self.s.lastStoneWeightII([5]), 5)

    def test_two_equal_stones(self):
        self.assertEqual(self.s.lastStoneWeightII([3, 3]), 0)

    def test_two_unequal_stones(self):
        self.assertEqual(self.s.lastStoneWeightII([3, 7]), 4)

    def test_all_same(self):
        self.assertEqual(self.s.lastStoneWeightII([4, 4, 4, 4]), 0)


if __name__ == "__main__":
    unittest.main()
