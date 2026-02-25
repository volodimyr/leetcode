import unittest
from integer_break import Solution


class TestIntegerBreak(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_small_values(self):
        self.assertEqual(self.solution.integerBreak(2), 1)
        self.assertEqual(self.solution.integerBreak(3), 2)

    def test_basic_cases(self):
        self.assertEqual(self.solution.integerBreak(4), 4)   # 2 * 2
        self.assertEqual(self.solution.integerBreak(5), 6)   # 2 * 3
        self.assertEqual(self.solution.integerBreak(6), 9)   # 3 * 3
        self.assertEqual(self.solution.integerBreak(7), 12)  # 3 * 4
        self.assertEqual(self.solution.integerBreak(8), 18)  # 3 * 3 * 2

    def test_larger_values(self):
        self.assertEqual(self.solution.integerBreak(10), 36)
        self.assertEqual(self.solution.integerBreak(15), 243)
        self.assertEqual(self.solution.integerBreak(20), 1458)

    def test_edge_case_one(self):
        # According to problem constraints (LeetCode 343),
        # n >= 2, but we test 1 for completeness
        self.assertEqual(self.solution.integerBreak(1), 0)


if __name__ == "__main__":
    unittest.main()