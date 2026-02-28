import unittest
from fish import Solution


class TestFindMaxFish(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [
            [0, 2, 1, 0],
            [4, 0, 0, 3],
            [1, 0, 0, 4],
            [0, 3, 2, 0]
        ]
        self.assertEqual(self.sol.findMaxFish(grid), 7)

    def test_example_2(self):
        grid = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ]
        self.assertEqual(self.sol.findMaxFish(grid), 1)

    def test_all_land(self):
        grid = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(self.sol.findMaxFish(grid), 0)

    def test_single_cell_water(self):
        grid = [[5]]
        self.assertEqual(self.sol.findMaxFish(grid), 5)

    def test_single_connected_component(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        # Entire grid is one connected water component
        self.assertEqual(self.sol.findMaxFish(grid), 10)

    def test_multiple_components(self):
        grid = [
            [1, 0, 2],
            [0, 0, 0],
            [3, 0, 4]
        ]
        # Largest single cell is 4
        self.assertEqual(self.sol.findMaxFish(grid), 4)

    def test_complex_shape(self):
        grid = [
            [1, 1, 0],
            [0, 1, 0],
            [2, 0, 3]
        ]
        # First component: 1+1+1 = 3
        # Second: 2
        # Third: 3
        self.assertEqual(self.sol.findMaxFish(grid), 3)


if __name__ == "__main__":
    unittest.main()