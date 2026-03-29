import unittest
from game import Solution


class TestStoneGameII(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.stoneGameII([2, 7, 9, 4, 4]), 10)

    def test_example2(self):
        self.assertEqual(self.s.stoneGameII([1, 2, 3, 4, 5, 100]), 104)

    def test_single_pile(self):
        self.assertEqual(self.s.stoneGameII([5]), 5)

    def test_two_piles(self):
        # Alice takes both on first turn (X=1 or X=2, M=1 so max 2)
        self.assertEqual(self.s.stoneGameII([3, 7]), 10)

    def test_equal_piles(self):
        self.assertEqual(self.s.stoneGameII([1, 1, 1, 1]), 2)

    def test_increasing_piles(self):
        self.assertEqual(self.s.stoneGameII([1, 2, 3, 4]), 5)

    def test_all_same(self):
        self.assertEqual(self.s.stoneGameII([4, 4, 4, 4]), 8)


if __name__ == "__main__":
    unittest.main()
