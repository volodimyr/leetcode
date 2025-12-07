import unittest
from copy import deepcopy
from regions import Solution   # adjust import based on your file name


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_example_2(self):
        board = [["X"]]
        expected = [["X"]]
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_no_O(self):
        board = [
            ["X","X"],
            ["X","X"]
        ]
        expected = deepcopy(board)
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_all_O_on_border(self):
        board = [
            ["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]
        ]
        expected = deepcopy(board)   # none should flip because all connected to border
        self.sol.solve(board)
        self.assertEqual(board, expected)

    def test_single_region_fully_surrounded(self):
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","X"],
        ]
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
        ]
        self.sol.solve(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
