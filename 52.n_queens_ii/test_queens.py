import unittest
from queens import Solution


class TestTotalNQueens(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_n_equals_1(self):
        self.assertEqual(self.sol.totalNQueens(1), 1)

    def test_n_equals_2(self):
        self.assertEqual(self.sol.totalNQueens(2), 0)

    def test_n_equals_3(self):
        self.assertEqual(self.sol.totalNQueens(3), 0)

    def test_n_equals_4(self):
        self.assertEqual(self.sol.totalNQueens(4), 2)

    def test_n_equals_5(self):
        self.assertEqual(self.sol.totalNQueens(5), 10)

    def test_n_equals_6(self):
        self.assertEqual(self.sol.totalNQueens(6), 4)

    def test_n_equals_7(self):
        self.assertEqual(self.sol.totalNQueens(7), 40)

    def test_n_equals_8(self):
        self.assertEqual(self.sol.totalNQueens(8), 92)

    def test_n_equals_9(self):
        self.assertEqual(self.sol.totalNQueens(9), 352)


if __name__ == "__main__":
    unittest.main()