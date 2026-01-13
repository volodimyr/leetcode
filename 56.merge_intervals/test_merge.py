import unittest
from merge import Solution


class TestMergeIntervals(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_example_2_touching_intervals(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_example_3_unsorted_input(self):
        intervals = [[4,7],[1,4]]
        expected = [[1,7]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_single_interval(self):
        intervals = [[2,3]]
        expected = [[2,3]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_no_overlap(self):
        intervals = [[1,2],[3,4],[5,6]]
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_fully_nested_intervals(self):
        intervals = [[1,10],[2,3],[4,8]]
        expected = [[1,10]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_multiple_overlaps(self):
        intervals = [[1,4],[2,5],[7,9],[8,10]]
        expected = [[1,5],[7,10]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_same_start(self):
        intervals = [[1,3],[1,4],[1,2]]
        expected = [[1,4]]
        self.assertEqual(self.sol.merge(intervals), expected)

    def test_same_end(self):
        intervals = [[1,5],[2,5],[3,5]]
        expected = [[1,5]]
        self.assertEqual(self.sol.merge(intervals), expected)


if __name__ == "__main__":
    unittest.main()
