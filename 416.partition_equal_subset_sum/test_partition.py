import unittest
from partition import Solution


class TestCanPartition(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_example_true(self):
        self.assertTrue(self.solver.canPartition([1, 5, 11, 5]))

    def test_example_false(self):
        self.assertFalse(self.solver.canPartition([1, 2, 3, 5]))

    def test_single_element(self):
        self.assertFalse(self.solver.canPartition([1]))

    def test_two_equal_elements(self):
        self.assertTrue(self.solver.canPartition([2, 2]))

    def test_all_same_even_count(self):
        self.assertTrue(self.solver.canPartition([3, 3, 3, 3]))

    def test_all_same_odd_count(self):
        self.assertFalse(self.solver.canPartition([3, 3, 3]))

    def test_large_possible_partition(self):
        nums = [1] * 100 + [2] * 50  # total = 200
        self.assertTrue(self.solver.canPartition(nums))

    def test_large_impossible_partition(self):
        nums = [1] * 199  # total = 199 (odd)
        self.assertFalse(self.solver.canPartition(nums))

    def test_partition_with_duplicates(self):
        self.assertFalse(self.solver.canPartition([2, 2, 3, 5]))

    def test_edge_case_large_numbers(self):
        self.assertTrue(self.solver.canPartition([100, 100]))


if __name__ == "__main__":
    unittest.main()