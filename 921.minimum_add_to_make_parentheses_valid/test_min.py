import unittest

from min import Solution

class TestMinAddToMakeValid(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example1(self):
        """Test case from example 1: s = '())'"""
        self.assertEqual(self.solution.minAddToMakeValid("())"), 1)
    
    def test_example2(self):
        """Test case from example 2: s = '((('"""
        self.assertEqual(self.solution.minAddToMakeValid("((("), 3)
    
    # Edge cases
    def test_single_opening(self):
        """Single opening parenthesis"""
        self.assertEqual(self.solution.minAddToMakeValid("("), 1)
    
    def test_single_closing(self):
        """Single closing parenthesis"""
        self.assertEqual(self.solution.minAddToMakeValid(")"), 1)
    
    def test_already_valid(self):
        """Already valid parentheses string"""
        self.assertEqual(self.solution.minAddToMakeValid("()"), 0)
    
    def test_nested_valid(self):
        """Nested valid parentheses"""
        self.assertEqual(self.solution.minAddToMakeValid("(())"), 0)
    
    def test_multiple_pairs_valid(self):
        """Multiple valid pairs"""
        self.assertEqual(self.solution.minAddToMakeValid("()()()"), 0)
    
    # Unbalanced cases
    def test_only_opening(self):
        """Only opening parentheses"""
        self.assertEqual(self.solution.minAddToMakeValid("(((("), 4)
    
    def test_only_closing(self):
        """Only closing parentheses"""
        self.assertEqual(self.solution.minAddToMakeValid("))))"), 4)
    
    def test_more_opening_than_closing(self):
        """More opening than closing parentheses"""
        self.assertEqual(self.solution.minAddToMakeValid("((()"), 2)
    
    # Complex cases
    def test_mixed_imbalanced(self):
        """Mixed imbalanced parentheses"""
        self.assertEqual(self.solution.minAddToMakeValid("()))(("), 4)
    
    def test_alternating_invalid(self):
        """Alternating but starting with closing"""
        self.assertEqual(self.solution.minAddToMakeValid(")("), 2)
    
    def test_long_invalid(self):
        """Long invalid string"""
        s = "(" * 500 + ")" * 300
        self.assertEqual(self.solution.minAddToMakeValid(s), 200)
    
    # Special patterns
    def test_all_nested_opening(self):
        """All opening parentheses nested style"""
        self.assertEqual(self.solution.minAddToMakeValid("(((((("), 6)
    
    def test_closing_then_opening(self):
        """Closing parentheses followed by opening"""
        self.assertEqual(self.solution.minAddToMakeValid("))))((("), 7)
    
    def test_valid_with_complex_nesting(self):
        """Valid string with complex nesting"""
        self.assertEqual(self.solution.minAddToMakeValid("((()()))"), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)