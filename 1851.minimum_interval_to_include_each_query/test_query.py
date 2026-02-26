import unittest
from query import Solution


class TestMinInterval(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        intervals = [[1,4],[2,4],[3,6],[4,4]]
        queries = [2,3,4,5]
        expected = [3,3,1,4]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_example_2(self):
        intervals = [[2,3],[2,5],[1,8],[20,25]]
        queries = [2,19,5,22]
        expected = [2,-1,4,6]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_no_intervals_match(self):
        intervals = [[1,2],[3,4]]
        queries = [5,6,7]
        expected = [-1,-1,-1]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_single_interval_multiple_queries(self):
        intervals = [[5,10]]
        queries = [5,7,10,4,11]
        expected = [6,6,6,-1,-1]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_duplicate_queries(self):
        intervals = [[1,5],[2,3]]
        queries = [2,2,3,3]
        expected = [2,2,2,2]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_large_interval_small_inside(self):
        intervals = [[1,100],[50,60],[55,55]]
        queries = [55]
        expected = [1]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_query_on_boundary(self):
        intervals = [[1,5],[6,10]]
        queries = [1,5,6,10]
        expected = [5,5,5,5]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)

    def test_unsorted_input(self):
        intervals = [[5,7],[1,3],[2,6]]
        queries = [6,2,4]
        expected = [3,3,5]
        self.assertEqual(self.sol.minInterval(intervals, queries), expected)


if __name__ == "__main__":
    unittest.main()