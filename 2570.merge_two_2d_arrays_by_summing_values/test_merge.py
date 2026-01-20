import unittest
from merge import Solution


class TestMergeArrays(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [[1, 2], [2, 3], [4, 5]]
        nums2 = [[1, 4], [3, 2], [4, 1]]
        expected = [[1, 6], [2, 3], [3, 2], [4, 6]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)

    def test_example_2(self):
        nums1 = [[2, 4], [3, 6], [5, 5]]
        nums2 = [[1, 3], [4, 3]]
        expected = [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)

    def test_one_array_empty_like_behavior(self):
        nums1 = [[1, 1], [2, 2]]
        nums2 = []
        expected = [[1, 1], [2, 2]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)

    def test_all_common_ids(self):
        nums1 = [[1, 10], [2, 20]]
        nums2 = [[1, 5], [2, 5]]
        expected = [[1, 15], [2, 25]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)

    def test_single_element_each_same_id(self):
        nums1 = [[1, 100]]
        nums2 = [[1, 200]]
        expected = [[1, 300]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)

    def test_single_element_each_different_id(self):
        nums1 = [[1, 100]]
        nums2 = [[2, 200]]
        expected = [[1, 100], [2, 200]]
        self.assertEqual(self.solution.mergeArrays(nums1, nums2), expected)


if __name__ == "__main__":
    unittest.main()
