import unittest
from effort import Solution

class TestMinimumEffortPath(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        heights = [[1,2,2],[3,8,2],[5,3,5]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 2)

    def test_example_2(self):
        heights = [[1,2,3],[3,8,4],[5,3,5]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 1)

    def test_example_3(self):
        heights = [[1,2,1,1,1],
                   [1,2,1,2,1],
                   [1,2,1,2,1],
                   [1,2,1,2,1],
                   [1,1,1,2,1]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 0)

    def test_single_cell(self):
        heights = [[5]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 0)

    def test_single_row(self):
        heights = [[1,10,6,7]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 9)

    def test_single_column(self):
        heights = [[1],[10],[6],[7]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 9)

    def test_flat_grid(self):
        heights = [[3,3,3],[3,3,3],[3,3,3]]
        self.assertEqual(self.sol.minimumEffortPath(heights), 0)

if __name__ == "__main__":
    unittest.main()
