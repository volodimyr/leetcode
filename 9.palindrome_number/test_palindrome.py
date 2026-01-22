import unittest
from palindrome import Solution

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_negative_number(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    def test_not_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(10))

    def test_single_digit_numbers(self):
        # All single-digit numbers are palindromes
        for i in range(10):
            self.assertTrue(self.solution.isPalindrome(i))

    def test_large_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(123454321))

    def test_large_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(123456789))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))

if __name__ == "__main__":
    unittest.main()
