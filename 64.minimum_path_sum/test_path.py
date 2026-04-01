import unittest
from path import Solution

class TestMinPathSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(self.sol.minPathSum(grid), 7)

    def test_example_2(self):
        grid = [[1,2,3],[4,5,6]]
        self.assertEqual(self.sol.minPathSum(grid), 12)

    def test_single_cell(self):
        grid = [[5]]
        self.assertEqual(self.sol.minPathSum(grid), 5)

    def test_single_row(self):
        grid = [[1,2,3,4]]
        self.assertEqual(self.sol.minPathSum(grid), 10)

    def test_single_column(self):
        grid = [[1],[2],[3],[4]]
        self.assertEqual(self.sol.minPathSum(grid), 10)

    def test_all_zeros(self):
        grid = [[0,0],[0,0]]
        self.assertEqual(self.sol.minPathSum(grid), 0)

    def test_large_values(self):
        grid = [[200,200],[200,200]]
        self.assertEqual(self.sol.minPathSum(grid), 600)

    def test_prefer_down_then_right(self):
        grid = [[1,100],[1,1]]
        self.assertEqual(self.sol.minPathSum(grid), 3)

    def test_prefer_right_then_down(self):
        grid = [[1,1,100],[100,1,1]]
        self.assertEqual(self.sol.minPathSum(grid), 4)

    def test_rectangular_grid(self):
        grid = [
            [1,2,5],
            [3,2,1]
        ]
        self.assertEqual(self.sol.minPathSum(grid), 6)


if __name__ == "__main__":
    unittest.main()