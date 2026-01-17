import unittest
from lemonade import Solution


class TestLemonadeChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # --- Basic examples from the problem ---
    def test_example_true(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 5, 10, 20]))

    def test_example_false(self):
        self.assertFalse(self.solution.lemonadeChange([5, 5, 10, 10, 20]))

    # --- Edge cases ---
    def test_single_customer_five(self):
        self.assertTrue(self.solution.lemonadeChange([5]))

    def test_single_customer_ten(self):
        self.assertFalse(self.solution.lemonadeChange([10]))

    def test_single_customer_twenty(self):
        self.assertFalse(self.solution.lemonadeChange([20]))

    # --- Greedy correctness ---
    def test_multiple_tens_then_twenty(self):
        self.assertFalse(self.solution.lemonadeChange([5, 5, 10, 10, 20]))

    def test_prefer_ten_over_fives(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 5, 10, 5, 20]))

    def test_three_fives_for_twenty(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 5, 20]))

    def test_insufficient_fives_for_twenty(self):
        self.assertFalse(self.solution.lemonadeChange([5, 10, 20]))

    # --- Longer sequences ---
    def test_all_fives(self):
        self.assertTrue(self.solution.lemonadeChange([5] * 100))

    def test_valid_mixed_sequence(self):
        self.assertTrue(self.solution.lemonadeChange([5, 5, 10, 5, 20, 5, 10, 5, 20]))

    def test_invalid_mid_sequence(self):
        self.assertFalse(self.solution.lemonadeChange([5, 5, 10, 20, 20]))


if __name__ == "__main__":
    unittest.main()
