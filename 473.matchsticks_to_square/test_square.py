import unittest
from square import Solution


class TestMakesquare(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.makesquare([1, 1, 2, 2, 2]))

    def test_example2(self):
        self.assertFalse(self.s.makesquare([3, 3, 3, 3, 4]))

    def test_equal_sides(self):
        self.assertTrue(self.s.makesquare([1, 1, 1, 1]))

    def test_sum_not_divisible_by_4(self):
        self.assertFalse(self.s.makesquare([1, 1, 1]))

    def test_single_stick(self):
        self.assertFalse(self.s.makesquare([4]))

    def test_large_values(self):
        self.assertTrue(self.s.makesquare([100000000, 100000000, 100000000, 100000000]))

    def test_cannot_form_square(self):
        self.assertTrue(self.s.makesquare([5, 5, 5, 1, 4]))

    def test_multiple_sticks_per_side(self):
        self.assertTrue(self.s.makesquare([1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == "__main__":
    unittest.main()
