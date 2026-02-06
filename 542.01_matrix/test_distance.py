import unittest
from distance import Solution


class TestUpdateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_cell_zero(self):
        mat = [[0]]
        expected = [[0]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_single_cell_one(self):
        mat = [[1, 0]]
        expected = [[1, 0]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_basic_example(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        expected = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_no_adjacent_zero(self):
        mat = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expected = [
            [2, 1, 2],
            [1, 0, 1],
            [2, 1, 2]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_row(self):
        mat = [[1, 1, 0, 1]]
        expected = [[2, 1, 0, 1]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_column(self):
        mat = [
            [1],
            [1],
            [0],
            [1]
        ]
        expected = [
            [2],
            [1],
            [0],
            [1]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_multiple_zeros(self):
        mat = [
            [0, 1, 1],
            [1, 1, 0],
            [1, 1, 1]
        ]
        expected = [
            [0, 1, 1],
            [1, 1, 0],
            [2, 2, 1]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)


if __name__ == "__main__":
    unittest.main()
