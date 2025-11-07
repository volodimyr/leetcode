import heapq
import unittest

from happy import Solution

class TestLongestHappyString(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def is_valid_happy_string(self, s, a, b, c):
        """Helper function to validate if a string is a valid happy string"""
        # Check no three consecutive same characters
        for i in range(len(s) - 2):
            if s[i] == s[i+1] == s[i+2]:
                return False
        
        # Check character counts don't exceed limits
        count_a = s.count('a')
        count_b = s.count('b')
        count_c = s.count('c')
        
        if count_a > a or count_b > b or count_c > c:
            return False
        
        # Check only contains a, b, c
        for char in s:
            if char not in ['a', 'b', 'c']:
                return False
        
        return True
    
    def test_example_1(self):
        """Test case: a=1, b=1, c=7"""
        result = self.solution.longestDiverseString(1, 1, 7)
        self.assertTrue(self.is_valid_happy_string(result, 1, 1, 7))
        self.assertEqual(len(result), 8)  # Should use most characters
    
    def test_example_2(self):
        """Test case: a=7, b=1, c=0"""
        result = self.solution.longestDiverseString(7, 1, 0)
        self.assertTrue(self.is_valid_happy_string(result, 7, 1, 0))
        self.assertEqual(len(result), 5)  # "aabaa" is optimal
    
    def test_equal_distribution(self):
        """Test case: a=2, b=2, c=2"""
        result = self.solution.longestDiverseString(2, 2, 2)
        self.assertTrue(self.is_valid_happy_string(result, 2, 2, 2))
        self.assertEqual(len(result), 6)  # Should use all characters
    
    def test_single_character_type(self):
        """Test case: a=5, b=0, c=0"""
        result = self.solution.longestDiverseString(5, 0, 0)
        self.assertTrue(self.is_valid_happy_string(result, 5, 0, 0))
        self.assertEqual(len(result), 2)  # Can only use "aa"
    
    def test_two_character_types(self):
        """Test case: a=4, b=1, c=0"""
        result = self.solution.longestDiverseString(4, 1, 0)
        self.assertTrue(self.is_valid_happy_string(result, 4, 1, 0))
        self.assertEqual(len(result), 5)  # "aabaa" or "abaaa" etc.
    
    def test_all_zeros(self):
        """Test case: a=0, b=0, c=1 (minimum valid input)"""
        result = self.solution.longestDiverseString(0, 0, 1)
        self.assertTrue(self.is_valid_happy_string(result, 0, 0, 1))
        self.assertEqual(len(result), 1)
    
    def test_large_imbalance(self):
        """Test case: a=100, b=1, c=1"""
        result = self.solution.longestDiverseString(100, 1, 1)
        self.assertTrue(self.is_valid_happy_string(result, 100, 1, 1))
        # With such imbalance, we can't use all 'a's
        self.assertGreater(len(result), 4)
    
    def test_no_three_consecutive(self):
        """Verify no result contains three consecutive same characters"""
        test_cases = [
            (1, 1, 7),
            (7, 1, 0),
            (3, 3, 3),
            (10, 5, 2),
            (0, 8, 11)
        ]
        
        for a, b, c in test_cases:
            result = self.solution.longestDiverseString(a, b, c)
            for i in range(len(result) - 2):
                self.assertFalse(
                    result[i] == result[i+1] == result[i+2],
                    f"Found three consecutive '{result[i]}' in result: {result}"
                )
    
    def test_uses_all_when_possible(self):
        """Test that all characters are used when possible"""
        # Balanced case - should use all
        result = self.solution.longestDiverseString(2, 2, 2)
        self.assertEqual(len(result), 6)
        
        # Nearly balanced - should use all
        result = self.solution.longestDiverseString(3, 3, 2)
        self.assertEqual(len(result), 8)
    
    def test_edge_case_small_values(self):
        """Test small values"""
        result = self.solution.longestDiverseString(1, 1, 1)
        self.assertTrue(self.is_valid_happy_string(result, 1, 1, 1))
        self.assertEqual(len(result), 3)
    
    def test_optimal_length_verification(self):
        """Verify the solution produces optimal or near-optimal lengths"""
        # When one letter dominates heavily
        result = self.solution.longestDiverseString(0, 8, 11)
        # Maximum possible is limited by the constraint
        self.assertGreaterEqual(len(result), 18)  # Should get most chars


if __name__ == '__main__':
    unittest.main(verbosity=2)