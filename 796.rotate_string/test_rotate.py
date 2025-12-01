import unittest
from rotate import Solution
# --- Unit Tests ---
class TestRotateString(unittest.TestCase):
    """
    Unit tests for the rotateString method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # 1. Standard Valid Rotation (Example 1)
    def test_example_valid_rotation(self):
        """Test a case where goal is a valid rotation of s."""
        s = "abcde"
        goal = "cdeab"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")

    # 2. Standard Invalid Rotation (Example 2)
    def test_example_invalid_rotation(self):
        """Test a case where goal is NOT a valid rotation of s."""
        s = "abcde"
        goal = "abced"
        self.assertFalse(self.solution.rotateString(s, goal),
                         f"Input: s='{s}', goal='{goal}'. Expected False.")

    # 3. No Rotation (Identical Strings)
    def test_identical_strings(self):
        """Test case where strings are identical (0 shifts)."""
        s = "hello"
        goal = "hello"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")

    # 4. Single Shift
    def test_single_shift(self):
        """Test case with exactly one shift."""
        s = "abcd"
        goal = "bcda"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")
    
    # 5. Length Mismatch
    def test_length_mismatch(self):
        """Test case where string lengths are different (must return False)."""
        s = "abc"
        goal = "abcd"
        self.assertFalse(self.solution.rotateString(s, goal),
                         f"Input: s='{s}', goal='{goal}'. Expected False (Length mismatch).")

    # 6. Length Mismatch (Reverse)
    def test_length_mismatch_reverse(self):
        """Test case where goal is shorter."""
        s = "abcd"
        goal = "abc"
        self.assertFalse(self.solution.rotateString(s, goal),
                         f"Input: s='{s}', goal='{goal}'. Expected False (Length mismatch).")
    
    # 7. One-Character String
    def test_one_char_string(self):
        """Test case with the minimum string length (1)."""
        s = "a"
        goal = "a"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")
    
    # 8. One-Character String Mismatch
    def test_one_char_mismatch(self):
        """Test case with one-character strings that don't match."""
        s = "a"
        goal = "b"
        self.assertFalse(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected False.")

    # 9. All Characters Same (Edge Case)
    def test_all_same_char(self):
        """Test strings consisting of the same repeated character."""
        s = "aaaaa"
        goal = "aaaaa"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")

    # 10. Complex Invalid Case (Same characters, wrong arrangement)
    def test_complex_invalid_arrangement(self):
        """Test a case where 'goal' has the same character count but is not a rotation."""
        s = "waterbottle"
        goal = "erbottlewat"
        # s+s = "waterbottlewaterbottle" -> "erbottlewat" is in it
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")

    # 11. Final character shift
    def test_full_shift(self):
        """Test case where s needs n shifts to become goal (n=length)."""
        s = "xyz"
        goal = "xyz"
        self.assertTrue(self.solution.rotateString(s, goal),
                        f"Input: s='{s}', goal='{goal}'. Expected True.")


if __name__ == "__main__":
    unittest.main()