import unittest
from flow import Solution

class TestPacificAtlantic(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        heights = [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
        expected = [
            [0,4],[1,3],[1,4],[2,2],
            [3,0],[3,1],[4,0]
        ]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        heights = [[1]]
        expected = [[0,0]]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_flat_grid(self):
        heights = [
            [5,5,5],
            [5,5,5],
            [5,5,5]
        ]
        # Every cell can reach both oceans
        expected = [[r, c] for r in range(3) for c in range(3)]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_increasing_diagonal(self):
        heights = [
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5]
        ]
        # Only last column + last row + corners
        expected = [
            [0,2],[1,2],[2,2],
            [2,0],[2,1]
        ]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_single_row(self):
        heights = [[1, 2, 2, 3, 1]]
        # Pacific: index 0
        # Atlantic: index -1
        expected = [[0,0], [0,4], [0,3], [0,2], [0,1]]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)

    def test_single_column(self):
        heights = [
            [1],
            [3],
            [2],
            [4]
        ]
        # Pacific: top
        # Atlantic: bottom
        expected = [[0,0],[1,0],[2,0],[3,0]]
        result = self.sol.pacificAtlantic(heights)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
