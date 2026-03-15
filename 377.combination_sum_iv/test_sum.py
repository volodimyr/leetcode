import unittest
from typing import List
from sum import Solution


class TestCombinationSum4(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.combinationSum4([1, 2, 3], 4), 7)

    def test_example2(self):
        self.assertEqual(self.solution.combinationSum4([9], 3), 0)

    def test_single_element_exact(self):
        self.assertEqual(self.solution.combinationSum4([3], 3), 1)

    def test_target_one(self):
        self.assertEqual(self.solution.combinationSum4([1, 2, 3], 1), 1)

    def test_target_equals_num(self):
        self.assertEqual(self.solution.combinationSum4([2, 3, 5], 5), 3)

    def test_order_matters(self):
        # [1,2] and [2,1] are different sequences
        self.assertEqual(self.solution.combinationSum4([1, 2], 3), 3)

    def test_large_target(self):
        self.assertIsInstance(self.solution.combinationSum4([1, 2, 3], 10), int)


if __name__ == "__main__":
    unittest.main()
