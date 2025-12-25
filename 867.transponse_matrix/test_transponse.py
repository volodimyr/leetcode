import unittest
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        
        return res


class TestTransposeMatrix(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_square_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_rectangular_more_rows(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        expected = [
            [1, 3, 5],
            [2, 4, 6]
        ]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_rectangular_more_columns(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        expected = [
            [1, 4],
            [2, 5],
            [3, 6]
        ]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_single_row(self):
        matrix = [[1, 2, 3, 4]]
        expected = [
            [1],
            [2],
            [3],
            [4]
        ]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_single_column(self):
        matrix = [
            [1],
            [2],
            [3]
        ]
        expected = [[1, 2, 3]]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_single_element(self):
        matrix = [[42]]
        expected = [[42]]
        self.assertEqual(self.solution.transpose(matrix), expected)

    def test_negative_and_large_values(self):
        matrix = [
            [-1, 10**9],
            [5, -10**9]
        ]
        expected = [
            [-1, 5],
            [10**9, -10**9]
        ]
        self.assertEqual(self.solution.transpose(matrix), expected)


if __name__ == "__main__":
    unittest.main()
