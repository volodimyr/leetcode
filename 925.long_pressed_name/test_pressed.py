import unittest
from pressed import Solution

# --- Unit Tests ---
class TestIsLongPressedName(unittest.TestCase):
    """
    Unit tests for the isLongPressedName method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # 1. Standard Case (Example 1)
    def test_example_valid(self):
        """Test the valid long press example."""
        name = "alex"
        typed = "aaleex"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 2. Invalid Case (Example 2)
    def test_example_invalid(self):
        """Test the invalid long press example (missing press)."""
        name = "saeed"
        typed = "ssaaedd"
        self.assertFalse(self.solution.isLongPressedName(name, typed),
                         f"Input: name='{name}', typed='{typed}'. Expected False.")

    # 3. No Long Press
    def test_no_long_press(self):
        """Test case where strings are identical."""
        name = "abc"
        typed = "abc"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 4. Full Long Press
    def test_all_long_pressed(self):
        """Test case where every character is long pressed."""
        name = "hello"
        typed = "hheeelllloo"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 5. Leading Long Press
    def test_leading_long_press(self):
        """Test case with only the first character long pressed."""
        name = "bar"
        typed = "bbaarr"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 6. Trailing Long Press
    def test_trailing_long_press(self):
        """Test case with only the last character long pressed."""
        name = "code"
        typed = "codeee"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 7. Different Character Mismatch
    def test_different_character_mismatch(self):
        """Test case where a non-matching character is introduced."""
        name = "abc"
        typed = "axbc"
        self.assertFalse(self.solution.isLongPressedName(name, typed),
                         f"Input: name='{name}', typed='{typed}'. Expected False.")

    # 8. Insufficient Characters in typed
    def test_insufficient_typed_char(self):
        """Test case where 'typed' is shorter than 'name' or a required press is missing."""
        name = "aabb"
        typed = "aab"
        self.assertFalse(self.solution.isLongPressedName(name, typed),
                         f"Input: name='{name}', typed='{typed}'. Expected False.")
    
    # 9. Complex case with multiple long presses
    def test_complex_long_press(self):
        """Test a more complex mixed case."""
        name = "zxcvb"
        typed = "zzxxccvvbbbb"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")

    # 10. Typed ends too early
    def test_typed_too_short(self):
        """Test case where typed runs out before name is completed."""
        name = "scaling"
        typed = "scal"
        self.assertFalse(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected False.")

    # 11. Empty name or typed (though constraints say 1 <= length)
    def test_empty_string_based_on_constraints(self):
        """Test with minimum length constraints (1)"""
        name = "a"
        typed = "a"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")
        
        name = "a"
        typed = "aa"
        self.assertTrue(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected True.")
        
        name = "aa"
        typed = "a"
        self.assertFalse(self.solution.isLongPressedName(name, typed),
                        f"Input: name='{name}', typed='{typed}'. Expected False.")

if __name__ == '__main__':
    # You can run the tests by uncommenting the line below and executing the script.
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("Run `unittest.main()` to execute the tests.")