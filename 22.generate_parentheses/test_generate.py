import unittest
from typing import List
from generate import Solution

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def is_valid_parenthesis(self, s: str) -> bool:
        """Helper to verify if a string has valid parentheses"""
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    def test_example1(self):
        """Test Example 1: n=3"""
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example2(self):
        """Test Example 2: n=1"""
        n = 1
        expected = ["()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(result, expected)
    
    def test_n_equals_2(self):
        """Test n=2"""
        n = 2
        expected = ["(())", "()()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_n_equals_4(self):
        """Test n=4"""
        n = 4
        result = self.solution.generateParenthesis(n)
        # Verify count: Catalan number C(4) = 14
        self.assertEqual(len(result), 14)
        # Verify all are valid and unique
        self.assertEqual(len(result), len(set(result)))
        for combo in result:
            self.assertTrue(self.is_valid_parenthesis(combo))
            self.assertEqual(len(combo), 2 * n)
    
    def test_all_valid_parentheses(self):
        """Test that all generated combinations are valid"""
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            for combo in result:
                self.assertTrue(self.is_valid_parenthesis(combo), 
                              f"Invalid parentheses: {combo} for n={n}")
    
    def test_correct_length(self):
        """Test that all combinations have correct length"""
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            for combo in result:
                self.assertEqual(len(combo), 2 * n, 
                               f"Wrong length for {combo} with n={n}")
    
    def test_no_duplicates(self):
        """Test that there are no duplicate combinations"""
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            self.assertEqual(len(result), len(set(result)), 
                           f"Duplicates found for n={n}")
    
    def test_catalan_numbers(self):
        """Test that the count matches Catalan numbers"""
        catalan = {
            1: 1,   # C(1) = 1
            2: 2,   # C(2) = 2
            3: 5,   # C(3) = 5
            4: 14,  # C(4) = 14
            5: 42,  # C(5) = 42
            6: 132, # C(6) = 132
            7: 429, # C(7) = 429
            8: 1430 # C(8) = 1430
        }
        for n, expected_count in catalan.items():
            result = self.solution.generateParenthesis(n)
            self.assertEqual(len(result), expected_count, 
                           f"Wrong count for n={n}")
    
    def test_min_constraint(self):
        """Test minimum constraint: n=1"""
        n = 1
        result = self.solution.generateParenthesis(n)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "()")
    
    def test_max_constraint(self):
        """Test maximum constraint: n=8"""
        n = 8
        result = self.solution.generateParenthesis(n)
        self.assertEqual(len(result), 1430)  # C(8) = 1430
        # Verify all are valid
        for combo in result:
            self.assertTrue(self.is_valid_parenthesis(combo))
            self.assertEqual(len(combo), 16)
    
    def test_balanced_parentheses(self):
        """Test that each combination has equal opening and closing"""
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            for combo in result:
                open_count = combo.count('(')
                close_count = combo.count(')')
                self.assertEqual(open_count, n, 
                               f"Wrong open count in {combo}")
                self.assertEqual(close_count, n, 
                               f"Wrong close count in {combo}")
    
    def test_specific_patterns(self):
        """Test that specific known patterns are included"""
        # For n=3, check specific patterns
        n = 3
        result = self.solution.generateParenthesis(n)
        
        # All opens then all closes
        self.assertIn("((()))", result)
        # All alternating
        self.assertIn("()()()", result)
        # Nested in middle
        self.assertIn("()(())", result)
    
    def test_opening_always_before_closing(self):
        """Test that at any point, opens >= closes"""
        for n in range(1, 6):
            result = self.solution.generateParenthesis(n)
            for combo in result:
                opens = 0
                closes = 0
                for char in combo:
                    if char == '(':
                        opens += 1
                    else:
                        closes += 1
                    self.assertGreaterEqual(opens, closes, 
                                          f"Invalid sequence in {combo}")


if __name__ == '__main__':
    unittest.main()