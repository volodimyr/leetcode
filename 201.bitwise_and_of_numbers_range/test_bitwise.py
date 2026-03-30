import unittest
from bitwise import Solution

class TestRangeBitwiseAnd(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(5, 7), 4)

    def test_example2(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 0), 0)

    def test_example3(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(1, 2147483647), 0)

    def test_same_left_right(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(7, 7), 7)

    def test_consecutive(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(6, 7), 6)

    def test_power_of_two_boundary(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(8, 15), 8)

    def test_cross_power_of_two(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(7, 8), 0)

    def test_zero_range(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 1), 0)

    def test_large_same(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(2147483647, 2147483647), 2147483647)


if __name__ == '__main__':
    unittest.main(verbosity=2)
