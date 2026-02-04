import unittest
from intersection import Solution


class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(set(result), {2})

    def test_example_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(set(result), {4, 9})

    def test_no_intersection(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [])

    def test_one_empty_array(self):
        self.assertEqual(self.solution.intersection([], [1, 2, 3]), [])
        self.assertEqual(self.solution.intersection([1, 2, 3], []), [])

    def test_both_empty_arrays(self):
        self.assertEqual(self.solution.intersection([], []), [])

    def test_all_elements_same(self):
        nums1 = [2, 2, 2]
        nums2 = [2, 2]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(set(result), {2})

    def test_single_element_intersection(self):
        nums1 = [1]
        nums2 = [1]
        result = self.solution.intersection(nums1, nums2)
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main()
