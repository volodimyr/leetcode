import unittest
from typing import List
from servers import Solution

class TestCountServers(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_server(self):
        grid = [[1]]
        self.assertEqual(self.sol.countServers(grid), 0)

    def test_no_communication(self):
        grid = [[1, 0],
                [0, 1]]
        self.assertEqual(self.sol.countServers(grid), 0)

    def test_simple_communication(self):
        grid = [[1, 0],
                [1, 1]]
        self.assertEqual(self.sol.countServers(grid), 3)

    def test_row_communication(self):
        grid = [[1, 1, 1]]
        self.assertEqual(self.sol.countServers(grid), 3)

    def test_column_communication(self):
        grid = [[1],
                [1],
                [1]]
        self.assertEqual(self.sol.countServers(grid), 3)

    def test_mixed_case(self):
        grid = [
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        self.assertEqual(self.sol.countServers(grid), 4)

    def test_all_zeros(self):
        grid = [[0, 0],
                [0, 0]]
        self.assertEqual(self.sol.countServers(grid), 0)

    def test_dense_grid(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(self.sol.countServers(grid), 4)


if __name__ == "__main__":
    unittest.main()
