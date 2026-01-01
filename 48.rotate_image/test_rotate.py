import unittest
from rotate import Solution


class TestRotateImage(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_3x3_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_4x4_matrix(self):
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_matrix(self):
        matrix = [[42]]
        expected = [[42]]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_negative_numbers(self):
        matrix = [
            [-1, -2],
            [-3, -4]
        ]
        expected = [
            [-3, -1],
            [-4, -2]
        ]
        self.sol.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_in_place(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        original_id = id(matrix)
        self.sol.rotate(matrix)
        self.assertEqual(id(matrix), original_id)


if __name__ == "__main__":
    unittest.main()
