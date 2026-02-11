import unittest
from reverse import Solution


class TestReverseInteger(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # Basic cases
    def test_positive_number(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test_negative_number(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_trailing_zero(self):
        self.assertEqual(self.sol.reverse(120), 21)

    def test_zero(self):
        self.assertEqual(self.sol.reverse(0), 0)

    def test_single_digit(self):
        self.assertEqual(self.sol.reverse(7), 7)
        self.assertEqual(self.sol.reverse(-7), -7)

    # Boundary values
    def test_int_max_boundary(self):
        self.assertEqual(self.sol.reverse(1463847412), 2147483641)

    def test_int_min_boundary(self):
        self.assertEqual(self.sol.reverse(-1463847412), -2147483641)

    # Overflow cases
    def test_overflow_positive(self):
        # Reverses to 9646324351 > 2^31 - 1
        self.assertEqual(self.sol.reverse(1534236469), 0)

    def test_overflow_negative(self):
        # Reverses to -9646324351 < -2^31
        self.assertEqual(self.sol.reverse(-1534236469), 0)

    # Exact 32-bit limits
    def test_exact_int_max(self):
        self.assertEqual(self.sol.reverse(2147483647), 0)

    def test_exact_int_min(self):
        self.assertEqual(self.sol.reverse(-2147483648), 0)


if __name__ == "__main__":
    unittest.main()
