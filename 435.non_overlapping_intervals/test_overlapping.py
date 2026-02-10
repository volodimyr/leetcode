import unittest
from overlapping import Solution

class TestEraseOverlapIntervals(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 1)

    def test_example_2(self):
        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 2)

    def test_example_3(self):
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 0)

    def test_single_interval(self):
        intervals = [[1, 5]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 0)

    def test_already_non_overlapping(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 0)

    def test_fully_overlapping(self):
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 3)

    def test_touching_intervals(self):
        intervals = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 0)

    def test_negative_intervals(self):
        intervals = [[-5, -1], [-3, 0], [1, 3]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 1)

    def test_unsorted_input(self):
        intervals = [[3, 4], [1, 2], [2, 3]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 0)

    def test_same_start_different_end(self):
        intervals = [[1, 4], [1, 3], [1, 2]]
        self.assertEqual(self.sol.eraseOverlapIntervals(intervals), 2)


if __name__ == "__main__":
    unittest.main()
