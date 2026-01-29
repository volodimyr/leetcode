import unittest
from divisor import Solution

class TestGCDOfStrings(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.sol.gcdOfStrings("ABCABC", "ABC"),
            "ABC"
        )

    def test_example_2(self):
        self.assertEqual(
            self.sol.gcdOfStrings("ABABAB", "ABAB"),
            "AB"
        )

    def test_example_3(self):
        self.assertEqual(
            self.sol.gcdOfStrings("LEET", "CODE"),
            ""
        )

    def test_example_4(self):
        self.assertEqual(
            self.sol.gcdOfStrings("AAAAAB", "AAA"),
            ""
        )

    def test_identical_strings(self):
        self.assertEqual(
            self.sol.gcdOfStrings("AAAA", "AAAA"),
            "AAAA"
        )

    def test_one_char_repetition(self):
        self.assertEqual(
            self.sol.gcdOfStrings("BBBBBB", "BBB"),
            "BBB"
        )

    def test_no_common_divisor(self):
        self.assertEqual(
            self.sol.gcdOfStrings("ABCDEF", "ABC"),
            ""
        )

    def test_single_character_strings(self):
        self.assertEqual(
            self.sol.gcdOfStrings("A", "A"),
            "A"
        )

    def test_different_single_characters(self):
        self.assertEqual(
            self.sol.gcdOfStrings("A", "B"),
            ""
        )

if __name__ == "__main__":
    unittest.main()
