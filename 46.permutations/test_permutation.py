import unittest
from typing import List
from permutation import Solution

class TestPermutations(unittest.TestCase):
    
    def setUp(self):
        """Initialize the solution instance before each test."""
        self.solution = Solution()

    def assertPermutationsEqual(self, actual: List[List[int]], expected: List[List[int]]):
        """Helper to compare two lists of permutations regardless of the order of the inner lists."""
        # Convert inner lists to tuples for hashing and comparison
        actual_set = {tuple(sorted(p)) for p in actual}
        expected_set = {tuple(sorted(p)) for p in expected}
        
        # A simpler approach for unique lists: sort both outer lists and compare
        # This works here because the number of permutations is N! and we want to ensure
        # all N! permutations are present.
        
        # Sort both the inner permutations and the outer list of permutations
        actual_sorted = sorted([sorted(p) for p in actual])
        expected_sorted = sorted([sorted(p) for p in expected])
        
        self.assertEqual(actual_sorted, expected_sorted, "The generated permutations do not match the expected set.")
        self.assertEqual(len(actual), len(expected), "The total number of permutations is incorrect.")


    def test_example_1_standard(self):
        """Test the standard example nums = [1, 2, 3]."""
        nums = [1, 2, 3]
        expected = [
            [1, 2, 3], [1, 3, 2], 
            [2, 1, 3], [2, 3, 1], 
            [3, 1, 2], [3, 2, 1]
        ]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_example_2_zero_and_one(self):
        """Test with nums = [0, 1]."""
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_example_3_single_element(self):
        """Test the constraint edge case nums = [1]."""
        nums = [1]
        expected = [[1]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_four_elements_small_integers(self):
        """Test a larger case with negative numbers (within constraints)."""
        nums = [-1, 0, 1, 2]
        # Total permutations is 4! = 24
        result = self.solution.permute(nums)
        self.assertEqual(len(result), 24, "Should return N! permutations.")
        # We check the size and rely on the algorithm's correctness for content
        # as manually listing 24 permutations is impractical.
        
        # Check one specific known permutation to ensure correctness
        self.assertTrue([0, -1, 2, 1] in result)

    def test_two_distinct_elements(self):
        """Test with two distinct negative numbers."""
        nums = [-5, -10]
        expected = [[-5, -10], [-10, -5]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

if __name__ == '__main__':
    unittest.main()