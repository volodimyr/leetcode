import unittest
from insert import Solution

class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        expected = [[1,5],[6,9]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_example2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        expected = [[1,2],[3,10],[12,16]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_empty_intervals(self):
        intervals = []
        newInterval = [5,7]
        expected = [[5,7]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_no_overlap_before(self):
        intervals = [[5,7],[8,10]]
        newInterval = [1,3]
        expected = [[1,3],[5,7],[8,10]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_no_overlap_after(self):
        intervals = [[1,2],[3,4]]
        newInterval = [5,6]
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_full_overlap(self):
        intervals = [[2,3],[5,7],[8,10]]
        newInterval = [1,12]
        expected = [[1,12]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_overlap_multiple(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [0,9]
        expected = [[0,10],[12,16]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_single_interval_merge(self):
        intervals = [[1,5]]
        newInterval = [2,3]
        expected = [[1,5]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

    def test_adjacent_intervals(self):
        intervals = [[1,2],[3,5]]
        newInterval = [2,3]
        expected = [[1,5]]
        self.assertEqual(self.sol.insert(intervals, newInterval), expected)

if __name__ == "__main__":
    unittest.main()
