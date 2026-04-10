import unittest
from enclaves import Solution


class TestNumEnclaves(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
        self.assertEqual(self.sol.numEnclaves(grid), 3)

    def test_example2(self):
        grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
        self.assertEqual(self.sol.numEnclaves(grid), 0)

    def test_all_land(self):
        grid = [[1,1],[1,1]]
        self.assertEqual(self.sol.numEnclaves(grid), 0)

    def test_all_sea(self):
        grid = [[0,0],[0,0]]
        self.assertEqual(self.sol.numEnclaves(grid), 0)

    def test_single_enclosed(self):
        grid = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(self.sol.numEnclaves(grid), 1)

    def test_boundary_land(self):
        grid = [[1,0,0],[0,1,0],[0,0,1]]
        self.assertEqual(self.sol.numEnclaves(grid), 1)

    def test_large_enclosed_island(self):
        grid = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,0,0,0,0],
        ]
        self.assertEqual(self.sol.numEnclaves(grid), 8)


if __name__ == "__main__":
    unittest.main()
