import unittest

from permutation import Solution

class TestCheckInclusion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example1(self):
        """s2 contains permutation 'ba' of s1 'ab'"""
        self.assertTrue(self.solution.checkInclusion("ab", "eidbaooo"))
    
    def test_example2(self):
        """s2 does not contain any permutation of s1"""
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))
    
    # Edge cases
    def test_s1_longer_than_s2(self):
        """s1 is longer than s2, impossible to find permutation"""
        self.assertFalse(self.solution.checkInclusion("abcd", "abc"))
    
    def test_equal_strings(self):
        """s1 and s2 are identical"""
        self.assertTrue(self.solution.checkInclusion("abc", "abc"))
    
    def test_single_character_match(self):
        """Both strings are single characters that match"""
        self.assertTrue(self.solution.checkInclusion("a", "a"))
    
    def test_single_character_no_match(self):
        """Both strings are single characters that don't match"""
        self.assertFalse(self.solution.checkInclusion("a", "b"))
    
    def test_permutation_at_beginning(self):
        """Permutation appears at the start of s2"""
        self.assertTrue(self.solution.checkInclusion("ab", "baabc"))
    
    def test_permutation_at_end(self):
        """Permutation appears at the end of s2"""
        self.assertTrue(self.solution.checkInclusion("ab", "xyzba"))
    
    def test_permutation_in_middle(self):
        """Permutation appears in the middle of s2"""
        self.assertTrue(self.solution.checkInclusion("ab", "xbay"))
    
    # Character frequency tests
    def test_repeated_characters_match(self):
        """s1 has repeated characters and permutation exists"""
        self.assertTrue(self.solution.checkInclusion("aab", "cbaabaaa"))
    
    def test_all_same_character(self):
        """All characters are the same"""
        self.assertTrue(self.solution.checkInclusion("aaa", "aaaaaaa"))
    
    def test_all_same_character_insufficient(self):
        """Not enough of the same character in s2"""
        self.assertFalse(self.solution.checkInclusion("aaa", "aa"))
    
    # Complex cases
    def test_multiple_permutations(self):
        """Multiple permutations exist in s2"""
        self.assertTrue(self.solution.checkInclusion("abc", "cbaxyzabc"))
    
    def test_overlapping_windows(self):
        """Test sliding window with overlapping patterns"""
        self.assertTrue(self.solution.checkInclusion("ab", "aabb"))
    
    def test_almost_match(self):
        """Almost has permutation but one character is wrong"""
        self.assertFalse(self.solution.checkInclusion("abc", "abxc"))
    
    def test_subset_but_not_permutation(self):
        """s2 contains all characters but not in correct window"""
        self.assertFalse(self.solution.checkInclusion("abc", "axbxc"))
    
    # Alphabet tests
    def test_full_alphabet(self):
        """Test with many different characters"""
        self.assertTrue(self.solution.checkInclusion("abcdefgh", "xyzabcdefgh"))
    
    def test_reverse_order(self):
        """Permutation is reverse of s1"""
        self.assertTrue(self.solution.checkInclusion("abc", "cba"))
    
    # Length edge cases
    def test_s1_length_1_in_long_s2(self):
        """Single character s1 in long s2"""
        self.assertTrue(self.solution.checkInclusion("a", "abcdefghijk"))
    
    def test_s1_length_1_not_in_s2(self):
        """Single character s1 not in s2"""
        self.assertFalse(self.solution.checkInclusion("a", "bcdefg"))
    
    def test_long_s1_exact_match(self):
        """Long s1 that exactly matches s2"""
        s = "abcdefghijklmnop"
        self.assertTrue(self.solution.checkInclusion(s, s))
    
    # Tricky cases
    def test_extra_occurrence(self):
        """Window has extra occurrence of a character"""
        self.assertTrue(self.solution.checkInclusion("ab", "aabb"))
    
    def test_character_appears_later(self):
        """Required character appears after the window"""
        self.assertFalse(self.solution.checkInclusion("abc", "abxc"))


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)