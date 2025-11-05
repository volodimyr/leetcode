import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_simple_duplicates(self):
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_example_2_multiple_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])
    
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])
    
    def test_all_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_single_element(self):
        nums = [1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_two_identical_elements(self):
        nums = [1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_two_different_elements(self):
        nums = [1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_duplicates_at_start(self):
        nums = [1, 1, 1, 2, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_duplicates_at_end(self):
        nums = [1, 2, 3, 4, 4, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_duplicates_in_middle(self):
        nums = [1, 2, 2, 2, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_pairs_of_duplicates(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_negative_numbers(self):
        nums = [-3, -3, -2, -1, -1, 0, 0, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-3, -2, -1, 0, 1])
    
    def test_all_negative_duplicates(self):
        nums = [-5, -5, -5, -5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [-5])
    
    def test_large_numbers_with_duplicates(self):
        nums = [100, 100, 200, 300, 300, 300]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [100, 200, 300])
    
    def test_consecutive_duplicates_varying_length(self):
        nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])
    
    def test_zeros_with_duplicates(self):
        nums = [0, 0, 0, 1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [0, 1, 2])
    
    def test_empty_array(self):
        nums = []
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])


class TestRemoveDuplicatesProperties(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_modifies_array_in_place(self):
        nums = [1, 1, 2, 2, 3]
        original_id = id(nums)
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(id(nums), original_id)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])
    
    def test_first_k_elements_are_sorted(self):
        test_cases = [
            [1, 1, 2, 3, 3, 4],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [1, 2, 3, 4, 5],
        ]
        
        for nums in test_cases:
            original = nums.copy()
            k = self.solution.removeDuplicates(nums)
            
            for i in range(1, k):
                self.assertLessEqual(nums[i-1], nums[i], 
                    f"Array {original} not sorted after removal")
    
    def test_first_k_elements_are_unique(self):
        test_cases = [
            [1, 1, 2, 3, 3, 4],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [5, 5, 5, 5, 5],
        ]
        
        for nums in test_cases:
            original = nums.copy()
            k = self.solution.removeDuplicates(nums)
            unique_elements = set(nums[:k])
            
            self.assertEqual(len(unique_elements), k,
                f"Array {original} has duplicates in first {k} elements")
    
    def test_k_is_valid_length(self):
        test_cases = [
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            [1],
        ]
        
        for nums in test_cases:
            k = self.solution.removeDuplicates(nums)
            self.assertGreaterEqual(k, 1)
            self.assertLessEqual(k, len(nums))
    
    def test_relative_order_preserved(self):
        nums = [1, 1, 2, 3, 3, 4, 5, 5]
        expected = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(nums[:k], expected)


class TestRemoveDuplicatesEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_all_same_values_varying_length(self):
        for n in range(1, 11):
            nums = [5] * n
            k = self.solution.removeDuplicates(nums)
            self.assertEqual(k, 1)
            self.assertEqual(nums[0], 5)
    
    def test_no_duplicates_varying_length(self):
        for n in range(1, 11):
            nums = list(range(n))
            expected = nums.copy()
            k = self.solution.removeDuplicates(nums)
            self.assertEqual(k, n)
            self.assertEqual(nums[:k], expected)


if __name__ == '__main__':
    unittest.main()