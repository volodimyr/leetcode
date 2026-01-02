import unittest
from missing import Solution

class TestFirstMissingPositive(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_example_2(self):
        nums = [3, 4, -1, 1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 2)

    def test_example_3(self):
        nums = [7, 8, 9, 11, 12]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_single_element_positive(self):
        nums = [1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 2)

    def test_single_element_negative(self):
        nums = [-1]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_all_consecutive(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 6)

    def test_with_duplicates(self):
        nums = [1, 1, 2, 2]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_unsorted_with_gap(self):
        nums = [2, 3, 7, 6, 8, -1, -10, 15]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_missing_middle(self):
        nums = [1, 2, 4, 5]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_large_values_ignored(self):
        nums = [100, 200, 1, 2]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_all_negatives_and_zero(self):
        nums = [-3, -2, -1, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)


if __name__ == "__main__":
    unittest.main()
