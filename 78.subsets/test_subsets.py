import unittest
from subsets import Solution

class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def assertSubsetsEqual(self, result, expected):
        """Helper method to compare subsets regardless of order"""
        # Convert lists to sets of tuples for comparison
        result_set = {tuple(sorted(subset)) for subset in result}
        expected_set = {tuple(sorted(subset)) for subset in expected}
        self.assertEqual(result_set, expected_set)
        self.assertEqual(len(result), len(expected))
    
    def test_example1(self):
        """Test case from example 1"""
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)
    
    def test_example2(self):
        """Test case from example 2"""
        nums = [0]
        expected = [[], [0]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)
    
    def test_two_elements(self):
        """Test with two elements"""
        nums = [1, 2]
        expected = [[], [1], [2], [1, 2]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, 0, 1]
        expected = [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)
    
    def test_all_negative(self):
        """Test with all negative numbers"""
        nums = [-5, -3, -1]
        expected = [[], [-5], [-3], [-5, -3], [-1], [-5, -1], [-3, -1], [-5, -3, -1]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)
    
    def test_four_elements(self):
        """Test with four elements"""
        nums = [1, 2, 3, 4]
        result = self.solution.subsets(nums)
        # Power set of 4 elements should have 2^4 = 16 subsets
        self.assertEqual(len(result), 16)
        # Check empty set is present
        self.assertIn([], result)
        # Check full set is present
        self.assertTrue(any(sorted(subset) == [1, 2, 3, 4] for subset in result))
    
    def test_correct_count(self):
        """Verify the number of subsets is 2^n"""
        for n in range(1, 6):
            nums = list(range(n))
            result = self.solution.subsets(nums)
            expected_count = 2 ** n
            self.assertEqual(len(result), expected_count, 
                           f"For n={n}, expected {expected_count} subsets")
    
    def test_no_duplicates(self):
        """Ensure no duplicate subsets in result"""
        nums = [1, 2, 3]
        result = self.solution.subsets(nums)
        # Convert to set of tuples to check for duplicates
        result_tuples = [tuple(sorted(subset)) for subset in result]
        self.assertEqual(len(result_tuples), len(set(result_tuples)))
    
    def test_empty_subset_included(self):
        """Verify empty subset is always included"""
        test_cases = [[1], [1, 2], [1, 2, 3], [-1, 0, 1]]
        for nums in test_cases:
            result = self.solution.subsets(nums)
            self.assertIn([], result, f"Empty subset missing for nums={nums}")
    
    def test_full_set_included(self):
        """Verify full set is always included"""
        test_cases = [[1], [1, 2], [1, 2, 3], [-1, 0, 1]]
        for nums in test_cases:
            result = self.solution.subsets(nums)
            self.assertTrue(
                any(sorted(subset) == sorted(nums) for subset in result),
                f"Full set missing for nums={nums}"
            )
    
    def test_max_constraint(self):
        """Test with maximum constraint length"""
        nums = list(range(10))
        result = self.solution.subsets(nums)
        self.assertEqual(len(result), 2 ** 10)
    
    def test_boundary_values(self):
        """Test with boundary values from constraints"""
        nums = [-10, 10]
        expected = [[], [-10], [10], [-10, 10]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)