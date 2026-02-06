import unittest
from knight import Solution

class TestMinKnightMoves(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minKnightMoves(2, 1), 1)

    def test_example2(self):
        self.assertEqual(self.sol.minKnightMoves(5, 5), 4)

    def test_origin(self):
        # The knight is already at the target
        self.assertEqual(self.sol.minKnightMoves(0, 0), 0)

    def test_small_coordinates(self):
        self.assertEqual(self.sol.minKnightMoves(1, 1), 2)
        self.assertEqual(self.sol.minKnightMoves(1, 2), 1)
        self.assertEqual(self.sol.minKnightMoves(2, 2), 4)

    def test_negative_coordinates(self):
        # Symmetry should handle negative coordinates
        self.assertEqual(self.sol.minKnightMoves(-2, 1), 1)
        self.assertEqual(self.sol.minKnightMoves(-5, -5), 4)
        self.assertEqual(self.sol.minKnightMoves(5, -5), 4)

    def test_larger_coordinates(self):
        self.assertEqual(self.sol.minKnightMoves(300, 0), 150)  # roughly half, as knight can zig-zag
        self.assertEqual(self.sol.minKnightMoves(0, 300), 150)

if __name__ == "__main__":
    unittest.main()
