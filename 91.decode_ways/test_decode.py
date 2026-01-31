import unittest
from decode import Solution

class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        s = "12"
        expected = 2
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_example2(self):
        s = "226"
        expected = 3
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_example3(self):
        s = "06"
        expected = 0
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_single_digit(self):
        s = "8"
        expected = 1
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_leading_zero(self):
        s = "0"
        expected = 0
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_double_digit_invalid(self):
        s = "30"
        expected = 0  # '30' is invalid
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_long_valid(self):
        s = "11106"
        expected = 2  # "AAJF" and "KJF"
        self.assertEqual(self.sol.numDecodings(s), expected)

    def test_max_length(self):
        s = "1" * 100  # All ones
        # Number of ways for "111...1" of length 100 is Fibonacci(101)
        # We'll just check it returns an integer > 0
        self.assertTrue(isinstance(self.sol.numDecodings(s), int))
        self.assertGreater(self.sol.numDecodings(s), 0)

if __name__ == "__main__":
    unittest.main()
