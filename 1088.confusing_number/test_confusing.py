import unittest
from confusing import Solution


class TestConfusingNumber(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # Basic valid confusing numbers
    def test_single_digit_confusing(self):
        self.assertTrue(self.solution.confusingNumber(6))
        self.assertTrue(self.solution.confusingNumber(9))

    def test_multi_digit_confusing(self):
        self.assertTrue(self.solution.confusingNumber(89))
        self.assertFalse(self.solution.confusingNumber(69))
        self.assertTrue(self.solution.confusingNumber(8101))

    # Not confusing (same after rotation)
    def test_not_confusing_same_after_rotation(self):
        self.assertFalse(self.solution.confusingNumber(0))
        self.assertFalse(self.solution.confusingNumber(1))
        self.assertFalse(self.solution.confusingNumber(8))
        self.assertFalse(self.solution.confusingNumber(11))
        self.assertFalse(self.solution.confusingNumber(88))
        self.assertFalse(self.solution.confusingNumber(101))

    # Contains invalid digits
    def test_invalid_digits(self):
        self.assertFalse(self.solution.confusingNumber(2))
        self.assertFalse(self.solution.confusingNumber(7))
        self.assertFalse(self.solution.confusingNumber(25))
        self.assertFalse(self.solution.confusingNumber(347))

    # Leading zero after rotation case
    def test_leading_zero_case(self):
        # 8000 -> 0008 -> 8
        self.assertTrue(self.solution.confusingNumber(8000))


if __name__ == "__main__":
    unittest.main()