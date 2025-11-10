import unittest

from typing import List
from comb_sum import Solution

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.sol.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = self.sol.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test_example_3(self):
        candidates = [2]
        target = 1
        expected = []
        result = self.sol.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test_single_candidate_exact_match(self):
        candidates = [4]
        target = 8
        expected = [[4, 4]]
        result = self.sol.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)

    def test_no_combinations(self):
        candidates = [5, 10, 12]
        target = 3
        expected = []
        result = self.sol.combinationSum(candidates, target)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
