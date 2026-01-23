import unittest
from excel import Solution


class TestConvertToTitle(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_letter(self):
        self.assertEqual(self.solution.convertToTitle(1), "A")
        self.assertEqual(self.solution.convertToTitle(26), "Z")

    def test_double_letters(self):
        self.assertEqual(self.solution.convertToTitle(27), "AA")
        self.assertEqual(self.solution.convertToTitle(28), "AB")
        self.assertEqual(self.solution.convertToTitle(52), "AZ")
        self.assertEqual(self.solution.convertToTitle(53), "BA")

    def test_triple_letters(self):
        self.assertEqual(self.solution.convertToTitle(701), "ZY")
        self.assertEqual(self.solution.convertToTitle(702), "ZZ")
        self.assertEqual(self.solution.convertToTitle(703), "AAA")

    def test_large_values(self):
        self.assertEqual(self.solution.convertToTitle(18278), "ZZZ")
        self.assertEqual(self.solution.convertToTitle(16384), "XFD")  # Excel max column

    def test_min_value(self):
        self.assertEqual(self.solution.convertToTitle(1), "A")


if __name__ == "__main__":
    unittest.main()
