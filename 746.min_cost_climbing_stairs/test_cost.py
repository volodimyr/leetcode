import unittest
from cost import Solution

class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        cost = [10, 15, 20]
        expected = 15
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_example_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_two_elements_take_cheapest(self):
        cost = [5, 3]
        expected = 3
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_two_elements_equal(self):
        cost = [7, 7]
        expected = 7
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_increasing_costs(self):
        cost = [1, 2, 3, 4, 5]
        # Best: 2 + 4 = 6
        expected = 6
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_decreasing_costs(self):
        cost = [10, 8, 6, 4, 2]
        # Best: start 1 → skip → 3 → skip → top = 8 + 4 = 12
        expected = 12
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_zero_costs(self):
        cost = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_large_values(self):
        cost = [999] * 20
        # Always just pick any consistent route: all same → 999 * ceil(n/2)
        expected = 999 * 10
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)

    def test_single_step_zero_then_big(self):
        cost = [0, 100, 0, 100, 0]
        expected = 0
        self.assertEqual(self.s.minCostClimbingStairs(cost), expected)


if __name__ == "__main__":
    unittest.main()
