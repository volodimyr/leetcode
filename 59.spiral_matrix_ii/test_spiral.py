import unittest
from spiral import Solution


class TestSpiralMatrixII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        self.assertEqual(self.solution.generateMatrix(1), [[1]])

    def test_n_2(self):
        expected = [
            [1, 2],
            [4, 3]
        ]
        self.assertEqual(self.solution.generateMatrix(2), expected)

    def test_n_3(self):
        expected = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        self.assertEqual(self.solution.generateMatrix(3), expected)

    def test_n_4(self):
        expected = [
            [1,  2,  3,  4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9,  8,  7]
        ]
        self.assertEqual(self.solution.generateMatrix(4), expected)

    def test_matrix_contains_all_numbers(self):
        n = 5
        result = self.solution.generateMatrix(n)

        # Check dimensions
        self.assertEqual(len(result), n)
        self.assertTrue(all(len(row) == n for row in result))

        # Flatten and check all numbers from 1 to n^2 exist exactly once
        flattened = [num for row in result for num in row]
        self.assertEqual(sorted(flattened), list(range(1, n*n + 1)))


if __name__ == "__main__":
    unittest.main()
