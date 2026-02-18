import unittest
from perfect import Solution

class TestNumSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.numSquares(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.numSquares(1), 1)

    def test_perfect_square(self):
        self.assertEqual(self.solution.numSquares(4), 1)
        self.assertEqual(self.solution.numSquares(9), 1)
        self.assertEqual(self.solution.numSquares(16), 1)

    def test_sum_of_squares(self):
        self.assertEqual(self.solution.numSquares(12), 3)  # 4+4+4
        self.assertEqual(self.solution.numSquares(13), 2)  # 4+9
        self.assertEqual(self.solution.numSquares(17), 2)  # 16+1
        self.assertEqual(self.solution.numSquares(18), 2)  # 9+9

    def test_larger_numbers(self):
        self.assertEqual(self.solution.numSquares(100), 1)   # 10*10
        self.assertEqual(self.solution.numSquares(99), 3)    # 81+9+9

if __name__ == "__main__":
    unittest.main()
