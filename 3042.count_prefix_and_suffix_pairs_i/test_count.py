import unittest
from typing import List
from count import Solution

# Unit Test Class
class TestCountPrefixSuffixPairs(unittest.TestCase):
    
    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # --- Test Cases from Examples ---
    
    def test_example_1(self):
        """Test case from Example 1: ["a","aba","ababa","aa"] -> 4."""
        words = ["a", "aba", "ababa", "aa"]
        expected_output = 4
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        """Test case from Example 2: ["pa","papa","ma","mama"] -> 2."""
        words = ["pa", "papa", "ma", "mama"]
        expected_output = 2
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_example_3(self):
        """Test case from Example 3: ["abab","ab"] -> 0."""
        words = ["abab", "ab"]
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)
        
    # --- Custom Test Cases ---

    def test_empty_array(self):
        """Test case with an empty words array."""
        words = []
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_single_element_array(self):
        """Test case with a single-element words array."""
        words = ["hello"]
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_no_matches(self):
        """Test case where no pairs satisfy the condition."""
        words = ["apple", "banana", "cherry", "date"]
        expected_output = 0
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_full_matches(self):
        """Test case where multiple consecutive pairs match."""
        words = ["a", "aa", "aaa", "aaaa"]
        # (a, aa), (a, aaa), (a, aaaa) = 3
        # (aa, aaa), (aa, aaaa) = 2
        # (aaa, aaaa) = 1
        # Total = 3 + 2 + 1 = 6
        expected_output = 6
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_word_equals_prefix_and_suffix(self):
        """Test case where words[i] == words[j], which should not happen since i < j but is possible 
        in a more general case. Also test when words[i] is a full match of words[j]."""
        words = ["abc", "abc", "a", "a"]
        # Since i < j is required, we only consider:
        # (words[0], words[1]): ("abc", "abc") -> True (prefix=abc, suffix=abc)
        # (words[2], words[3]): ("a", "a") -> True (prefix=a, suffix=a)
        # Total = 2
        expected_output = 2
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

    def test_mixed_case(self):
        """Test case with a mix of short, long, matching, and non-matching words."""
        words = ["x", "xox", "ox", "y", "yoy"]
        # (x, xox) -> True
        # (x, ox) -> False
        # (x, y) -> False
        # (x, yoy) -> False
        # (xox, ox) -> False
        # (xox, y) -> False
        # (xox, yoy) -> False
        # (ox, y) -> False
        # (ox, yoy) -> False
        # (y, yoy) -> True
        # Total = 2
        expected_output = 2
        result = self.solution.countPrefixSuffixPairs(words)
        self.assertEqual(result, expected_output)

# This block allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)