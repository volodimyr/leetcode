import unittest

from number_of_sub_arr import Solution

class TestNumOfSubarrays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        arr = [2,2,2,2,5,5,5,8]
        k = 3
        threshold = 4
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 3)

    def test_example2(self):
        arr = [11,13,17,23,29,31,7,5,2,3]
        k = 3
        threshold = 5
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 6)

    def test_all_below_threshold(self):
        arr = [1,1,1,1,1]
        k = 2
        threshold = 3
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 0)

    def test_all_above_threshold(self):
        arr = [5,6,7,8,9]
        k = 2
        threshold = 4
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 4)

    def test_k_equals_length(self):
        arr = [2,4,6]
        k = 3
        threshold = 4
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 1)

    def test_threshold_zero(self):
        arr = [0,1,2,3,4]
        k = 2
        threshold = 0
        self.assertEqual(self.sol.numOfSubarrays(arr, k, threshold), 4)

if __name__ == "__main__":
    unittest.main()