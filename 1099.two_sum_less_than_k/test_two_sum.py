import unittest

from two_sum import Solution

class TestTwoSumLessThanK(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.twoSumLessThanK([34,23,1,24,75,33,54,8], 60), 58)

    def test_example2(self):
        self.assertEqual(self.s.twoSumLessThanK([10,20,30], 15), -1)

    def test_no_valid_pair(self):
        self.assertEqual(self.s.twoSumLessThanK([5,5], 10), -1)

    def test_all_pairs_valid(self):
        self.assertEqual(self.s.twoSumLessThanK([1,2,3], 100), 5)

    def test_single_valid_pair(self):
        self.assertEqual(self.s.twoSumLessThanK([1,1000], 1002), 1001)

    def test_two_elements_valid(self):
        self.assertEqual(self.s.twoSumLessThanK([3,4], 8), 7)

    def test_two_elements_invalid(self):
        self.assertEqual(self.s.twoSumLessThanK([3,4], 7), -1)

    def test_duplicates(self):
        self.assertEqual(self.s.twoSumLessThanK([5,5,5], 11), 10)

if __name__ == "__main__":
    unittest.main()
