import unittest
from valid import Solution


class TestValidWordAbbreviation(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_true(self):
        self.assertTrue(self.s.validWordAbbreviation("apple", "a3e"))

    def test_basic_false(self):
        self.assertFalse(self.s.validWordAbbreviation("international", "i9l"))

    def test_no_abbreviation(self):
        self.assertTrue(self.s.validWordAbbreviation("abbreviation", "abbreviation"))

    def test_full_number(self):
        self.assertTrue(self.s.validWordAbbreviation("implementation", "14"))

    def test_leading_zero(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "a012"))

    def test_zero_abbreviation(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "a0pple"))

    def test_adjacent_numbers(self):
        self.assertFalse(self.s.validWordAbbreviation("i", "i57n"))

    def test_number_exceeds_length(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "a10"))

    def test_wrong_char(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "b4e"))

    def test_abbr_too_short(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "a2"))

    def test_abbr_too_long(self):
        self.assertFalse(self.s.validWordAbbreviation("apple", "a3el"))

    def test_multi_segment(self):
        self.assertTrue(self.s.validWordAbbreviation("implementation", "imp4n5n"))

    def test_single_char_word(self):
        self.assertTrue(self.s.validWordAbbreviation("a", "a"))
        self.assertFalse(self.s.validWordAbbreviation("a", "b"))
        self.assertTrue(self.s.validWordAbbreviation("a", "1"))


if __name__ == "__main__":
    unittest.main()
