import unittest
from swim import Solution

class TestSwimInRisingWater(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0, 2],
                [1, 3]]
        self.assertEqual(self.solution.swimInWater(grid), 3)

    def test_example_2(self):
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]
        ]
        self.assertEqual(self.solution.swimInWater(grid), 16)

    def test_single_cell(self):
        grid = [[0]]
        self.assertEqual(self.solution.swimInWater(grid), 0)

    def test_straight_increasing_path(self):
        grid = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.assertEqual(self.solution.swimInWater(grid), 8)

    def test_detour_is_better(self):
        grid = [
            [0, 100, 101],
            [1, 2, 102],
            [3, 4, 5]
        ]
        # Best path avoids 100+, max elevation = 5
        self.assertEqual(self.solution.swimInWater(grid), 5)

    def test_snake_path(self):
        grid = [
            [0, 1, 6],
            [5, 2, 7],
            [4, 3, 8]
        ]
        self.assertEqual(self.solution.swimInWater(grid), 8)

    def test_large_values_early_block(self):
        grid = [
            [0, 10],
            [1, 2]
        ]
        self.assertEqual(self.solution.swimInWater(grid), 2)


if __name__ == "__main__":
    unittest.main()
