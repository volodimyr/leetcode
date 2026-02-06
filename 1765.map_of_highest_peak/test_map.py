import unittest
from map import Solution

class TestHighestPeak(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def assert_valid_height_map(self, isWater, height):
        """Helper to validate constraints"""
        m, n = len(isWater), len(isWater[0])

        # Same shape
        self.assertEqual(len(height), m)
        self.assertEqual(len(height[0]), n)

        for r in range(m):
            for c in range(n):
                # Non-negative
                self.assertGreaterEqual(height[r][c], 0)

                # Water cells must be 0
                if isWater[r][c] == 1:
                    self.assertEqual(height[r][c], 0)

                # Adjacent cells diff <= 1
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        self.assertLessEqual(
                            abs(height[r][c] - height[nr][nc]),
                            1
                        )

    def test_example_1(self):
        isWater = [
            [0, 1],
            [0, 0]
        ]
        res = self.sol.highestPeak([row[:] for row in isWater])
        self.assert_valid_height_map(isWater, res)
        self.assertEqual(max(map(max, res)), 2)

    def test_example_2(self):
        isWater = [
            [0, 0, 1],
            [1, 0, 0],
            [0, 0, 0]
        ]
        res = self.sol.highestPeak([row[:] for row in isWater])
        self.assert_valid_height_map(isWater, res)
        self.assertEqual(max(map(max, res)), 2)

    def test_all_water(self):
        isWater = [
            [1, 1],
            [1, 1]
        ]
        res = self.sol.highestPeak([row[:] for row in isWater])
        self.assertEqual(res, [
            [0, 0],
            [0, 0]
        ])

    def test_single_water_center(self):
        isWater = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        res = self.sol.highestPeak([row[:] for row in isWater])
        self.assert_valid_height_map(isWater, res)
        self.assertEqual(res[1][1], 0)
        self.assertEqual(max(map(max, res)), 2)

    def test_single_row(self):
        isWater = [[0, 0, 1, 0, 0]]
        res = self.sol.highestPeak([row[:] for row in isWater])
        self.assert_valid_height_map(isWater, res)
        self.assertEqual(res[0][2], 0)
        self.assertEqual(max(res[0]), 2)


if __name__ == "__main__":
    unittest.main()
