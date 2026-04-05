import unittest
from typing import List
from covered import Solution


class TestRemoveCoveredIntervals(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,4],[3,6],[2,8]]), 2)

    def test_example2(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,4],[2,3]]), 1)

    def test_single(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,2]]), 1)

    def test_no_covered(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,2],[3,4],[5,6]]), 3)

    def test_all_covered_by_one(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,10],[2,5],[3,7]]), 1)

    def test_same_start(self):
        self.assertEqual(self.s.removeCoveredIntervals([[1,4],[1,6]]), 1)

    def test_same_end(self):
        self.assertEqual(self.s.removeCoveredIntervals([[2,6],[1,6]]), 1)


if __name__ == "__main__":
    unittest.main()
