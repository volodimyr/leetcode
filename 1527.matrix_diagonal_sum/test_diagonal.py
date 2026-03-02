import unittest
from diagonal import Solution


class TestDiagonalSum(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(self.solver.diagonalSum(mat), 25)

    def test_example_2(self):
        mat = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(self.solver.diagonalSum(mat), 8)

    def test_single_element(self):
        mat = [[5]]
        self.assertEqual(self.solver.diagonalSum(mat), 5)

    def test_even_matrix(self):
        mat = [
            [2, 3],
            [4, 5]
        ]
        self.assertEqual(self.solver.diagonalSum(mat), 14)

    def test_larger_odd_matrix(self):
        mat = [
            [7, 3, 1, 9, 5],
            [2, 8, 6, 4, 0],
            [3, 5, 9, 7, 1],
            [8, 2, 4, 6, 3],
            [1, 7, 5, 2, 8]
        ]
        self.assertEqual(self.solver.diagonalSum(mat), 50)


if __name__ == "__main__":
    unittest.main()