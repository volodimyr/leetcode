import unittest
from move import Solution

class TestMoveZeroes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example_2(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_no_zeros(self):
        nums = [1, 2, 3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0])

    def test_zeros_at_end(self):
        nums = [1, 2, 3, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_single_non_zero(self):
        nums = [0, 0, 5, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [5, 0, 0, 0])

    def test_negative_numbers(self):
        nums = [0, -1, 0, -3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, -3, 4, 0, 0])

    def test_large_values(self):
        nums = [0, 2**31 - 1, 0, -2**31]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [2**31 - 1, -2**31, 0, 0])

if __name__ == "__main__":
    unittest.main()
