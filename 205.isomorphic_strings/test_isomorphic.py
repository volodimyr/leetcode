import unittest
from isomorphic import Solution


class TestIsomorphicStrings(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_true_1(self):
        self.assertTrue(self.sol.isIsomorphic("egg", "add"))

    def test_example_false(self):
        self.assertFalse(self.sol.isIsomorphic("foo", "bar"))

    def test_example_true_2(self):
        self.assertTrue(self.sol.isIsomorphic("paper", "title"))

    def test_single_character(self):
        self.assertTrue(self.sol.isIsomorphic("a", "b"))

    def test_same_string(self):
        self.assertTrue(self.sol.isIsomorphic("abc", "abc"))

    def test_length_mismatch(self):
        self.assertFalse(self.sol.isIsomorphic("ab", "abc"))

    def test_repeating_pattern_true(self):
        self.assertTrue(self.sol.isIsomorphic("abab", "cdcd"))

    def test_repeating_pattern_false(self):
        self.assertFalse(self.sol.isIsomorphic("abab", "cddc"))

    def test_ascii_characters(self):
        self.assertTrue(self.sol.isIsomorphic("!@#", "$%^"))

    def test_self_mapping_allowed(self):
        self.assertTrue(self.sol.isIsomorphic("aa", "aa"))

    def test_conflicting_mapping(self):
        self.assertFalse(self.sol.isIsomorphic("ab", "aa"))


if __name__ == "__main__":
    unittest.main()
