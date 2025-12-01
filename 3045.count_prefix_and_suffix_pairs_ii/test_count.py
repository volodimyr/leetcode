import unittest
from typing import List
from count import Solution

# --- User-Provided Code End (Corrected Logic) ---

class TestCountPrefixSuffixPairs(unittest.TestCase):
    
    def setUp(self):
        """Set up the Solution instance before each test."""
        # Use the corrected logic for testing
        self.solution = Solution()

    # --- Test Cases from Examples ---
    
    def test_example_1(self):
        """Test case from Example 1: ["a","aba","ababa","aa"] -> 4."""
        words = ["a", "aba", "ababa", "aa"]
        # Pairs: ("a", "aba"), ("a", "ababa"), ("a", "aa"), ("aba", "ababa")
        expected_output = 4
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        """Test case from Example 2: ["pa","papa","ma","mama"] -> 2."""
        words = ["pa", "papa", "ma", "mama"]
        # Pairs: ("pa", "papa"), ("ma", "mama")
        expected_output = 2
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_example_3(self):
        """Test case from Example 3: ["abab","ab"] -> 0."""
        words = ["abab", "ab"]
        # Pair: ("abab", "ab"). isPrefixAndSuffix("abab", "ab") is False.
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)
        
    # --- Custom Test Cases ---

    def test_no_matches(self):
        """Test case where no pairs satisfy the condition."""
        words = ["apple", "banana", "cherry", "date"]
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_full_matches_same_char(self):
        """Test case where multiple consecutive pairs match."""
        words = ["a", "aa", "aaa", "aaaa"]
        # (a, aa), (a, aaa), (a, aaaa) = 3
        # (aa, aaa), (aa, aaaa) = 2
        # (aaa, aaaa) = 1
        # Total = 6
        expected_output = 6
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)
        
    def test_long_words(self):
        """Test with longer, complex words."""
        words = ["level", "lever", "l", "levelxlevel"]
        # (level, lever) -> False
        # (level, l) -> False (L1 > L2)
        # (level, levelxlevel) -> False ('x' in the middle breaks suffix match)
        # (lever, l) -> False
        # (lever, levelxlevel) -> False
        # (l, levelxlevel) -> True (prefix: l, suffix: l)
        # Total = 1
        expected_output = 2
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_duplicates(self):
        """Test case with duplicate words."""
        words = ["ab", "ababa", "ab"]
        # Pair (0, 1): ("ab", "ababa") -> True
        # Pair (0, 2): ("ab", "ab") -> True
        # Pair (1, 2): ("ababa", "ab") -> False (L1 > L2)
        # Total = 2
        expected_output = 1
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)
        
    def test_prefix_only_or_suffix_only(self):
        """Test case where only one part of the condition is met."""
        words = ["abc", "abcd", "dabc"]
        # (abc, abcd) -> Prefix only (suffix is bcd)
        # (abc, dabc) -> Suffix only (prefix is dab)
        # (abcd, dabc) -> False
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)


# This block allows running the tests directly from the script
if __name__ == '__main__':
    # Setting verbosity to 2 for more detailed output
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)