import unittest
from remove_stars import Solution

class TestRemoveStars(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    # Example test cases
    def test_example1(self):
        self.assertEqual(self.s.removeStars("leet**cod*e"), "lecoe")
    
    def test_example2(self):
        self.assertEqual(self.s.removeStars("erase*****"), "")
    
    # Single character cases
    def test_single_char_no_star(self):
        self.assertEqual(self.s.removeStars("a"), "a")
    
    # Two character cases
    def test_two_chars_with_star(self):
        self.assertEqual(self.s.removeStars("a*"), "")
    
    def test_two_chars_no_star(self):
        self.assertEqual(self.s.removeStars("ab"), "ab")
    
    # No stars
    def test_no_stars(self):
        self.assertEqual(self.s.removeStars("abc"), "abc")
    
    def test_no_stars_long(self):
        self.assertEqual(self.s.removeStars("abcdefghij"), "abcdefghij")
    
    # Single star scenarios
    def test_single_star_at_end(self):
        self.assertEqual(self.s.removeStars("abc*"), "ab")
    
    def test_single_star_middle(self):
        self.assertEqual(self.s.removeStars("ab*c"), "ac")
    
    # Multiple consecutive stars
    def test_consecutive_stars(self):
        self.assertEqual(self.s.removeStars("abc***"), "")
    
    def test_consecutive_stars_partial(self):
        self.assertEqual(self.s.removeStars("abcd**"), "ab")
    
    def test_consecutive_stars_with_remainder(self):
        self.assertEqual(self.s.removeStars("abcde***fg"), "abfg")
    
    # Stars scattered throughout
    def test_scattered_stars(self):
        self.assertEqual(self.s.removeStars("a*b*c*"), "")
    
    # All stars (after initial chars)
    def test_all_removed(self):
        self.assertEqual(self.s.removeStars("abcd****"), "")
    
    def test_exact_balance(self):
        self.assertEqual(self.s.removeStars("aaa***"), "")
    
    # Stars at different positions
    def test_stars_at_beginning_middle_end(self):
        self.assertEqual(self.s.removeStars("ab*cd*ef*"), "ace")
    
    def test_multiple_groups(self):
        self.assertEqual(self.s.removeStars("ab**cd**ef"), "ef")
    
    def test_few_stars_many_chars(self):
        self.assertEqual(self.s.removeStars("abcdefgh*"), "abcdefg")
    
    # Complex patterns
    def test_complex_pattern1(self):
        self.assertEqual(self.s.removeStars("a*b*c*d*e*f*g"), "g")
    
    # Long strings
    def test_long_string_no_stars(self):
        s = "a" * 1000
        self.assertEqual(self.s.removeStars(s), s)
    
    def test_long_string_half_stars(self):
        # 1000 chars followed by 500 stars
        s = "a" * 1000 + "*" * 500
        self.assertEqual(self.s.removeStars(s), "a" * 500)
    
    def test_long_string_all_removed(self):
        # 1000 chars followed by 1000 stars
        s = "a" * 1000 + "*" * 1000
        self.assertEqual(self.s.removeStars(s), "")
    
    # Different characters
    def test_different_letters(self):
        self.assertEqual(self.s.removeStars("xyz*abc*def"), "xyabdef")
    
    def test_alphabet_with_stars(self):
        self.assertEqual(self.s.removeStars("abcdefg***"), "abcd")
    
    # Patterns that leave specific results
    def test_leave_first_char(self):
        self.assertEqual(self.s.removeStars("abcd***"), "a")
    
    def test_leave_last_char(self):
        self.assertEqual(self.s.removeStars("a*b*c*d"), "d")
    
    def test_leave_middle_chars(self):
        self.assertEqual(self.s.removeStars("abcdefgh****"), "abcd")
    
    def test_cascading_removals(self):
        self.assertEqual(self.s.removeStars("abc*d*e*f"), "abf")
    
    # Verify stack-like behavior (LIFO)
    def test_lifo_order(self):
        # Add abc, remove c, add d, remove d, result should be "ab"
        self.assertEqual(self.s.removeStars("abc*d*"), "ab")
    
    # Boundary with max constraint
    def test_near_max_length(self):
        # Test with string close to 10^5 length
        s = "a" * 50000 + "*" * 25000
        result = self.s.removeStars(s)
        self.assertEqual(len(result), 25000)
        self.assertEqual(result, "a" * 25000)

if __name__ == "__main__":
    unittest.main()