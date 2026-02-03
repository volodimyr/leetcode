import unittest
from trionic import Solution


class TestTrionicArray(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_true(self):
        self.assertTrue(self.sol.isTrionic([1, 3, 5, 4, 2, 6]))

    def test_example_false(self):
        self.assertFalse(self.sol.isTrionic([2, 1, 3]))

    def test_min_length(self):
        self.assertFalse(self.sol.isTrionic([1, 2, 3]))
        self.assertFalse(self.sol.isTrionic([3, 2, 1]))

    def test_all_increasing(self):
        self.assertFalse(self.sol.isTrionic([1, 2, 3, 4, 5]))

    def test_all_decreasing(self):
        self.assertFalse(self.sol.isTrionic([5, 4, 3, 2, 1]))

    def test_no_second_increase(self):
        self.assertFalse(self.sol.isTrionic([1, 3, 5, 4, 2]))

    def test_no_decrease(self):
        self.assertFalse(self.sol.isTrionic([1, 3, 5, 6, 7]))

    def test_equal_elements(self):
        self.assertFalse(self.sol.isTrionic([1, 2, 2, 1, 3]))
        self.assertFalse(self.sol.isTrionic([1, 3, 5, 5, 2, 6]))

    def test_valid_minimal_segments(self):
        self.assertTrue(self.sol.isTrionic([1, 2, 1, 2]))

    def test_long_valid(self):
        self.assertTrue(self.sol.isTrionic([1, 4, 7, 6, 3, 2, 5, 8]))

    def test_multiple_turns_invalid(self):
        self.assertFalse(self.sol.isTrionic([1, 3, 2, 4, 3, 5]))

    def test_negative_numbers(self):
        self.assertTrue(self.sol.isTrionic([-5, -3, -1, -2, -4, 0]))


if __name__ == "__main__":
    unittest.main()
