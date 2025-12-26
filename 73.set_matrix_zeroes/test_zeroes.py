import unittest
from zeroes import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1],
            ],
        )

    def test_example_2(self):
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0],
            ],
        )

    def test_single_element_zero(self):
        matrix = [[0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0]])

    def test_single_element_non_zero(self):
        matrix = [[5]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[5]])

    def test_no_zeroes(self):
        matrix = [
            [1, 2],
            [3, 4],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [1, 2],
                [3, 4],
            ],
        )

    def test_all_zeroes(self):
        matrix = [
            [0, 0],
            [0, 0],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [0, 0],
                [0, 0],
            ],
        )

    def test_zero_in_first_row(self):
        matrix = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [0, 0, 0],
                [0, 4, 5],
                [0, 7, 8],
            ],
        )

    def test_zero_in_first_column(self):
        matrix = [
            [1, 2, 3],
            [0, 4, 5],
            [6, 7, 8],
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(
            matrix,
            [
                [0, 2, 3],
                [0, 0, 0],
                [0, 7, 8],
            ],
        )


if __name__ == "__main__":
    unittest.main()
