import unittest
from multiply import Solution


class TestMultiplyStrings(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_digits(self):
        self.assertEqual(self.sol.multiply("2", "3"), "6")
        self.assertEqual(self.sol.multiply("9", "9"), "81")

    def test_zero(self):
        self.assertEqual(self.sol.multiply("0", "0"), "0")
        self.assertEqual(self.sol.multiply("0", "12345"), "0")
        self.assertEqual(self.sol.multiply("98765", "0"), "0")

    def test_small_numbers(self):
        self.assertEqual(self.sol.multiply("12", "34"), "408")
        self.assertEqual(self.sol.multiply("99", "99"), "9801")

    def test_different_lengths(self):
        self.assertEqual(self.sol.multiply("123", "4"), "492")
        self.assertEqual(self.sol.multiply("7", "456"), "3192")

    def test_examples(self):
        self.assertEqual(self.sol.multiply("123", "456"), "56088")

    def test_large_numbers(self):
        self.assertEqual(
            self.sol.multiply("123456789", "987654321"),
            "121932631112635269"
        )

    def test_power_of_ten(self):
        self.assertEqual(self.sol.multiply("1000", "1000"), "1000000")
        self.assertEqual(self.sol.multiply("1", "100000"), "100000")

    def test_commutativity(self):
        a = "314159"
        b = "271828"
        self.assertEqual(
            self.sol.multiply(a, b),
            self.sol.multiply(b, a)
        )


if __name__ == "__main__":
    unittest.main()
