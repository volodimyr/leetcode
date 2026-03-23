import unittest
from odd import Solution


class TestMaximumOddBinaryNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_one(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("010"), "001")

    def test_two_ones(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("0101"), "1001")

    def test_all_ones(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("111"), "111")

    def test_single_one_no_zeros(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("1"), "1")

    def test_many_zeros_one_one(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("0001"), "0001")

    def test_all_zeros_one_one(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("000100"), "000001")

    def test_multiple_ones_multiple_zeros(self):
        self.assertEqual(self.solution.maximumOddBinaryNumber("11010"), "11001")


if __name__ == "__main__":
    unittest.main()
