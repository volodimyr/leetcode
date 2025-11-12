import unittest
from typing import List
from sum import Solution

class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def assertCombinationsEqual(self, result, expected):
        """Helper to compare combinations regardless of order"""
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))
    
    def test_example1(self):
        """Test Example 1: [10,1,2,7,6,1,5], target=8"""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_example2(self):
        """Test Example 2: [2,5,2,1,2], target=5"""
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_single_element_match(self):
        """Test single element that matches target"""
        candidates = [1]
        target = 1
        expected = [[1]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_single_element_no_match(self):
        """Test single element that doesn't match target"""
        candidates = [1]
        target = 2
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)
    
    def test_no_solution(self):
        """Test when no combination sums to target"""
        candidates = [2, 3, 5]
        target = 1
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)
    
    def test_all_duplicates(self):
        """Test with all duplicate numbers"""
        candidates = [2, 2, 2, 2]
        target = 4
        expected = [[2, 2]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_multiple_duplicates(self):
        """Test with multiple sets of duplicates"""
        candidates = [1, 1, 1, 2, 2]
        target = 4
        expected = [[1, 1, 2], [2, 2]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_use_all_elements(self):
        """Test where all elements sum to target"""
        candidates = [1, 2, 3, 4]
        target = 10
        expected = [[1, 2, 3, 4]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_multiple_combinations(self):
        """Test with various possible combinations"""
        candidates = [1, 1, 2, 5, 6, 7, 10]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_three_duplicates(self):
        """Test with three of the same number"""
        candidates = [3, 3, 3]
        target = 9
        expected = [[3, 3, 3]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)
    
    def test_edge_case_min_values(self):
        """Test edge case with minimum constraint values"""
        candidates = [1]
        target = 1
        expected = [[1]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)


if __name__ == '__main__':
    unittest.main()