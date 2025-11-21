import unittest
from stairs import Solution

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    def test_small_values(self):
        self.assertEqual(self.s.climbStairs(1), 1)
        self.assertEqual(self.s.climbStairs(2), 2)
        self.assertEqual(self.s.climbStairs(3), 3)
        self.assertEqual(self.s.climbStairs(4), 5)

    def test_medium_values(self):
        # Fibonacci sequence logic
        self.assertEqual(self.s.climbStairs(5), 8)
        self.assertEqual(self.s.climbStairs(6), 13)
        self.assertEqual(self.s.climbStairs(7), 21)

    def test_larger_value(self):
        # Warning: with naive recursion this may run slow!
        self.assertEqual(self.s.climbStairs(10), 89)

    def test_typical_leetcode_examples(self):
        self.assertEqual(self.s.climbStairs(2), 2)
        self.assertEqual(self.s.climbStairs(3), 3)


if __name__ == "__main__":
    unittest.main()
