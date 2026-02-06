import unittest
from add import Solution

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        # Example 1
        self.assertEqual(self.sol.addBinary("11", "1"), "100")
        # Example 2
        self.assertEqual(self.sol.addBinary("1010", "1011"), "10101")

    def test_single_digit(self):
        self.assertEqual(self.sol.addBinary("0", "0"), "0")
        self.assertEqual(self.sol.addBinary("1", "0"), "1")
        self.assertEqual(self.sol.addBinary("0", "1"), "1")
        self.assertEqual(self.sol.addBinary("1", "1"), "10")

    def test_different_lengths(self):
        self.assertEqual(self.sol.addBinary("1", "111"), "1000")
        self.assertEqual(self.sol.addBinary("101", "10"), "111")

    def test_leading_zeros(self):
        self.assertEqual(self.sol.addBinary("0001", "0010"), "0011")
        self.assertEqual(self.sol.addBinary("0000", "0"), "0000")

if __name__ == "__main__":
    unittest.main()
