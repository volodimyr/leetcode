import unittest

from repeating import Solution

class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example_1(self):
        """Replace two A's with B's or vice versa"""
        self.assertEqual(self.solution.characterReplacement("ABAB", 2), 4)
    
    def test_all_same_characters(self):
        """String with all same characters"""
        self.assertEqual(self.solution.characterReplacement("AAAA", 0), 4)
        self.assertEqual(self.solution.characterReplacement("AAAA", 2), 4)
    
    def test_k_equals_zero(self):
        """No replacements allowed"""
        self.assertEqual(self.solution.characterReplacement("ABCDE", 0), 1)
        self.assertEqual(self.solution.characterReplacement("AABBC", 0), 2)
    
    def test_k_equals_length(self):
        """k equals string length - can replace all"""
        self.assertEqual(self.solution.characterReplacement("ABCD", 4), 4)
        self.assertEqual(self.solution.characterReplacement("ABC", 3), 3)
    
    def test_long_sequence(self):
        """Longer sequences"""
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)
        self.assertEqual(self.solution.characterReplacement("AAAAABBBBB", 3), 8)
    
    def test_max_at_end(self):
        """Longest substring at the end"""
        self.assertEqual(self.solution.characterReplacement("ABCDDDD", 1), 5)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)