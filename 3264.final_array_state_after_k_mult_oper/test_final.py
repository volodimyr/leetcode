import unittest
from final import Solution

class TestGetFinalState(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_operation(self):
        nums = [2, 1, 3]
        k = 1
        multiplier = 2
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [2, 2, 3])

    def test_multiple_operations(self):
        nums = [1, 2, 3]
        k = 3
        multiplier = 2
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [4, 4, 3])

    def test_same_min_value_uses_lowest_index(self):
        nums = [1, 1, 2]
        k = 1
        multiplier = 3
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [3, 1, 2])

    def test_k_zero(self):
        nums = [5, 4, 3]
        k = 0
        multiplier = 10
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [5, 4, 3])

    def test_multiplier_one(self):
        nums = [1, 2, 3]
        k = 5
        multiplier = 1
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [1, 2, 3])

    def test_single_element(self):
        nums = [7]
        k = 4
        multiplier = 3
        result = self.sol.getFinalState(nums, k, multiplier)
        self.assertEqual(result, [7 * (3 ** 4)])


if __name__ == "__main__":
    unittest.main()
