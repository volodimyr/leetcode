import unittest
from max_subarr import Solution


class TestMaxProductSubarray(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # ----- Provided examples -----

    def test_example_1(self):
        self.assertEqual(self.solution.maxProduct([2, 3, -2, 4]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProduct([-2, 0, -1]), 0)

    # ----- Single element -----

    def test_single_positive(self):
        self.assertEqual(self.solution.maxProduct([5]), 5)

    def test_single_negative(self):
        self.assertEqual(self.solution.maxProduct([-5]), -5)

    def test_single_zero(self):
        self.assertEqual(self.solution.maxProduct([0]), 0)

    # ----- Zeros in array -----

    def test_with_zero_split(self):
        self.assertEqual(self.solution.maxProduct([0, 2]), 2)

    def test_multiple_zeros(self):
        self.assertEqual(self.solution.maxProduct([0, -2, 0]), 0)

    # ----- All negatives -----

    def test_even_negatives(self):
        self.assertEqual(self.solution.maxProduct([-1, -2, -3, -4]), 24)

    def test_odd_negatives(self):
        self.assertEqual(self.solution.maxProduct([-1, -2, -3]), 6)

    # ----- Mixed values -----

    def test_mixed_case_1(self):
        self.assertEqual(self.solution.maxProduct([2, -5, -2, -4, 3]), 24)

    def test_mixed_case_2(self):
        self.assertEqual(self.solution.maxProduct([-2, 3, -4]), 24)

    def test_mixed_case_3(self):
        self.assertEqual(self.solution.maxProduct([3, -1, 4]), 4)

    # ----- Larger case -----

    def test_long_array(self):
        nums = [1, -2, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxProduct(nums), 960)


if __name__ == "__main__":
    unittest.main()
