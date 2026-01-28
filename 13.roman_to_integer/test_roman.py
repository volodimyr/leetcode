import unittest
from roman import Solution


class TestRomanToInt(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_single_symbols(self):
        self.assertEqual(self.sol.romanToInt("I"), 1)
        self.assertEqual(self.sol.romanToInt("V"), 5)
        self.assertEqual(self.sol.romanToInt("X"), 10)
        self.assertEqual(self.sol.romanToInt("L"), 50)
        self.assertEqual(self.sol.romanToInt("C"), 100)
        self.assertEqual(self.sol.romanToInt("D"), 500)
        self.assertEqual(self.sol.romanToInt("M"), 1000)

    def test_simple_additive(self):
        self.assertEqual(self.sol.romanToInt("III"), 3)
        self.assertEqual(self.sol.romanToInt("VIII"), 8)
        self.assertEqual(self.sol.romanToInt("LVIII"), 58)

    def test_subtractive_pairs(self):
        self.assertEqual(self.sol.romanToInt("IV"), 4)
        self.assertEqual(self.sol.romanToInt("IX"), 9)
        self.assertEqual(self.sol.romanToInt("XL"), 40)
        self.assertEqual(self.sol.romanToInt("XC"), 90)
        self.assertEqual(self.sol.romanToInt("CD"), 400)
        self.assertEqual(self.sol.romanToInt("CM"), 900)

    def test_mixed_cases(self):
        self.assertEqual(self.sol.romanToInt("XIV"), 14)
        self.assertEqual(self.sol.romanToInt("XXIX"), 29)
        self.assertEqual(self.sol.romanToInt("MCMXCIV"), 1994)

    def test_edge_cases(self):
        self.assertEqual(self.sol.romanToInt("I"), 1)
        self.assertEqual(self.sol.romanToInt("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()
