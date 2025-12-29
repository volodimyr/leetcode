import unittest
from spiral import Solution


class TestSpiralOrder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        matrix = [[1]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1])

    def test_single_row(self):
        matrix = [[1, 2, 3, 4]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 3, 4])

    def test_single_column(self):
        matrix = [[1], [2], [3], [4]]
        self.assertEqual(self.solution.spiralOrder(matrix), [1, 2, 3, 4])

    def test_square_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_rectangular_matrix(self):
        matrix = [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9, 10, 11, 12]
        ]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_two_by_two(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expected = [1, 2, 4, 3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_negative_numbers(self):
        matrix = [
            [-1, -2, -3],
            [-4, -5, -6]
        ]
        expected = [-1, -2, -3, -6, -5, -4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)


if __name__ == "__main__":
    unittest.main()
