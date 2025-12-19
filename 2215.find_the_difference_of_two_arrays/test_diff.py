import unittest
from typing import List
from diff import Solution


class TestFindDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertResultEqual(self, result, expected):
        self.assertEqual(set(result[0]), set(expected[0]))
        self.assertEqual(set(result[1]), set(expected[1]))

    def test_example_1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        expected = [[1, 3], [4, 6]]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)

    def test_example_2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        expected = [[3], []]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)

    def test_no_common_elements(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = [[1, 2], [3, 4]]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)

    def test_all_elements_common(self):
        nums1 = [1, 2, 3]
        nums2 = [3, 2, 1]
        expected = [[], []]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)

    def test_negative_numbers(self):
        nums1 = [-1, -2, 3]
        nums2 = [-2, 4]
        expected = [[-1, 3], [4]]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)

    def test_single_element_arrays(self):
        nums1 = [1]
        nums2 = [2]
        expected = [[1], [2]]
        result = self.solution.findDifference(nums1, nums2)
        self.assertResultEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
