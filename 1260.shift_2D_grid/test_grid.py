import unittest
from grid import Solution

class TestShiftGrid(unittest.TestCase):
    def setUp(self):
        """Initialize the solution instance before each test."""
        self.solution = Solution()

    def test_example_1_single_shift(self):
        """Input: [[1,2,3],[4,5,6],[7,8,9]], k = 1 -> [[9,1,2],[3,4,5],[6,7,8]]"""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_example_2_multi_shift(self):
        """Input: A 4x4 grid, k = 4 (one full row shift)."""
        grid = [
            [3, 8, 1, 9],
            [19, 7, 2, 5],
            [4, 6, 11, 10],
            [12, 0, 21, 13]
        ]
        k = 4
        expected = [
            [12, 0, 21, 13],  # Last row moves to the top
            [3, 8, 1, 9],
            [19, 7, 2, 5],
            [4, 6, 11, 10]
        ]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_example_3_full_cycle(self):
        """Input: k = 9 (M=9, full cycle) -> returns original grid."""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 9
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_zero_shift(self):
        """k = 0 should return the original grid."""
        grid = [[1, 1], [1, 1]]
        k = 0
        expected = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_large_shift_modulo(self):
        """Test with a large k, ensuring the modulo operation works (k=10 should be k=1 for a 3x3 grid)."""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 10  # 10 % 9 = 1
        expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_single_row_grid(self):
        """Test with a 1x5 grid."""
        grid = [[1, 2, 3, 4, 5]]
        k = 2
        # Flat: [1, 2, 3, 4, 5] -> Shifted: [4, 5, 1, 2, 3]
        expected = [[4, 5, 1, 2, 3]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_single_column_grid(self):
        """Test with a 3x1 grid."""
        grid = [[1], [2], [3]]
        k = 1
        # Flat: [1, 2, 3] -> Shifted: [3, 1, 2]
        expected = [[3], [1], [2]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

    def test_shift_past_end_of_row(self):
        """Test a shift that crosses rows (k=2 for a 2x3 grid)."""
        grid = [[1, 2, 3], [4, 5, 6]]
        k = 2
        # Flat: [1, 2, 3, 4, 5, 6] -> Shifted: [5, 6, 1, 2, 3, 4]
        expected = [[5, 6, 1], [2, 3, 4]]
        self.assertEqual(self.solution.shiftGrid(grid, k), expected)

if __name__ == '__main__':
    unittest.main()