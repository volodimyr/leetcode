import unittest
from square import Solution


class TestValidWordSquare(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_valid_square_basic(self):
        words = ["abcd", "bnrt", "crmy", "dtye"]
        self.assertTrue(self.solution.validWordSquare(words))

    def test_valid_square_shorter_words(self):
        words = ["ball", "area", "lead", "lady"]
        self.assertTrue(self.solution.validWordSquare(words))

    def test_invalid_square_mismatch(self):
        words = ["abcd", "bnrt", "crm", "dt"]
        self.assertTrue(self.solution.validWordSquare(words))

    def test_invalid_square_missing_column(self):
        words = ["abc", "b"]
        self.assertFalse(self.solution.validWordSquare(words))

    def test_single_word(self):
        words = ["a"]
        self.assertTrue(self.solution.validWordSquare(words))

    def test_empty_strings(self):
        words = ["", "", ""]
        self.assertTrue(self.solution.validWordSquare(words))

    def test_asymmetric_lengths(self):
        words = ["ab", "ba", "c"]
        self.assertFalse(self.solution.validWordSquare(words))


if __name__ == "__main__":
    unittest.main()
