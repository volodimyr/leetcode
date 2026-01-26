import unittest
from valid import Solution


class TestCheckValidString(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Basic cases
    def test_empty_star(self):
        self.assertTrue(self.sol.checkValidString("*"))

    def test_simple_valid(self):
        self.assertTrue(self.sol.checkValidString("()"))

    def test_simple_invalid(self):
        self.assertFalse(self.sol.checkValidString(")"))

    # Examples from the problem
    def test_example_1(self):
        self.assertTrue(self.sol.checkValidString("()"))

    def test_example_2(self):
        self.assertTrue(self.sol.checkValidString("(*)"))

    def test_example_3(self):
        self.assertTrue(self.sol.checkValidString("(*))"))

    # Edge ordering cases (important!)
    def test_star_before_open(self):
        self.assertFalse(self.sol.checkValidString("*("))

    def test_open_before_star(self):
        self.assertTrue(self.sol.checkValidString("(*"))

    def test_multiple_stars(self):
        self.assertTrue(self.sol.checkValidString("(**)"))

    # Nested and complex
    def test_nested_valid(self):
        self.assertTrue(self.sol.checkValidString("(*()*)"))

    def test_nested_invalid(self):
        self.assertFalse(self.sol.checkValidString("((*))("))

    def test_unmatched_left(self):
        self.assertTrue(self.sol.checkValidString("((*)"))

    def test_unmatched_right(self):
        self.assertFalse(self.sol.checkValidString("())*"))

    # All stars
    def test_all_stars(self):
        self.assertTrue(self.sol.checkValidString("***"))

    # Long mixed case
    def test_long_mixed(self):
        self.assertTrue(self.sol.checkValidString("(*()(**)())"))


if __name__ == "__main__":
    unittest.main()
