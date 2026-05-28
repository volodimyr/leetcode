import unittest
from missing_ranges import Solution


class TestFindMissingRanges(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99),
            [[2, 2], [4, 49], [51, 74], [76, 99]]
        )

    def test_example2_single_element_no_missing(self):
        self.assertEqual(self.sol.findMissingRanges([-1], -1, -1), [])

    def test_empty_nums(self):
        self.assertEqual(self.sol.findMissingRanges([], 1, 5), [[1, 5]])

    def test_full_coverage(self):
        self.assertEqual(self.sol.findMissingRanges([0, 1, 2, 3], 0, 3), [])

    def test_missing_at_start(self):
        self.assertEqual(self.sol.findMissingRanges([3], 0, 5), [[0, 2], [4, 5]])

    def test_missing_at_end(self):
        self.assertEqual(self.sol.findMissingRanges([0], 0, 5), [[1, 5]])

    def test_single_gap(self):
        self.assertEqual(self.sol.findMissingRanges([1, 3], 1, 3), [[2, 2]])

    def test_negative_range(self):
        self.assertEqual(self.sol.findMissingRanges([-3, -1], -5, 0), [[-5, -4], [-2, -2], [0, 0]])

    def test_all_missing(self):
        self.assertEqual(self.sol.findMissingRanges([], -10**9, 10**9), [[-10**9, 10**9]])

    def test_lower_equals_upper_missing(self):
        self.assertEqual(self.sol.findMissingRanges([], 5, 5), [[5, 5]])

    def test_lower_equals_upper_present(self):
        self.assertEqual(self.sol.findMissingRanges([5], 5, 5), [])


if __name__ == "__main__":
    unittest.main()
