import unittest
from perfect import Solution


class TestIsPerfectSquare(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_perfect_square(self):
        self.assertTrue(self.s.isPerfectSquare(16))

    def test_not_perfect_square(self):
        self.assertFalse(self.s.isPerfectSquare(14))

    def test_one(self):
        self.assertTrue(self.s.isPerfectSquare(1))

    def test_large_perfect_square(self):
        self.assertTrue(self.s.isPerfectSquare(2147395600))  # 46340^2

    def test_large_non_perfect(self):
        self.assertFalse(self.s.isPerfectSquare(2147483647))


if __name__ == "__main__":
    unittest.main()
