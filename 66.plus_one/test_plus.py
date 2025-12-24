import unittest
from typing import List
from plus import Solution

class TestPlusOne(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_simple_increment(self):
        self.assertEqual(
            self.solution.plusOne([1, 2, 3]),
            [1, 2, 4]
        )

    def test_no_carry_middle(self):
        self.assertEqual(
            self.solution.plusOne([4, 3, 2, 1]),
            [4, 3, 2, 2]
        )

    def test_single_digit_no_carry(self):
        self.assertEqual(
            self.solution.plusOne([5]),
            [6]
        )

    def test_single_digit_with_carry(self):
        self.assertEqual(
            self.solution.plusOne([9]),
            [1, 0]
        )

    def test_multiple_carry(self):
        self.assertEqual(
            self.solution.plusOne([1, 9, 9]),
            [2, 0, 0]
        )

    def test_all_nines(self):
        self.assertEqual(
            self.solution.plusOne([9, 9, 9]),
            [1, 0, 0, 0]
        )

    def test_large_input(self):
        digits = [9] * 100
        expected = [1] + [0] * 100
        self.assertEqual(
            self.solution.plusOne(digits),
            expected
        )

    def test_trailing_zeros_after_carry(self):
        self.assertEqual(
            self.solution.plusOne([2, 9, 9, 9]),
            [3, 0, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
