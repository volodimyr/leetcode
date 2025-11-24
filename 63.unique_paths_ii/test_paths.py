import unittest
from paths import Solution

class TestUniquePathsWithObstacles(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        grid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 2)

    def test_example2(self):
        grid = [
            [0,1],
            [0,0]
        ]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 1)

    def test_single_cell_no_obstacle(self):
        grid = [[0]]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 1)

    def test_single_cell_with_obstacle(self):
        grid = [[1]]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 0)

    def test_first_cell_blocked(self):
        grid = [
            [1,0,0],
            [0,0,0]
        ]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 0)

    def test_last_cell_blocked(self):
        grid = [
            [0,0,0],
            [0,0,1]
        ]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 0)

    def test_full_row_blocked(self):
        grid = [
            [0,0,0],
            [1,1,1],
            [0,0,0]
        ]
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 0)

    def test_no_obstacles(self):
        grid = [
            [0,0],
            [0,0],
            [0,0]
        ]
        # Number of paths in 3x2 grid = 3
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 3)

    def test_large_no_obstacles(self):
        grid = [[0]*5 for _ in range(5)]
        # Unique paths for 5x5 = C(8,4) = 70
        self.assertEqual(self.s.uniquePathsWithObstacles(grid), 70)

if __name__ == "__main__":
    unittest.main()
