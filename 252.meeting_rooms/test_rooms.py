import unittest
from rooms import Solution, Interval

class TestCanAttendMeetings(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_intervals(self):
        self.assertTrue(self.s.canAttendMeetings([]))

    def test_single_interval(self):
        intervals = [Interval(5, 10)]
        self.assertTrue(self.s.canAttendMeetings(intervals))

    def test_no_conflicts(self):
        intervals = [Interval(5, 8), Interval(9, 15)]
        self.assertTrue(self.s.canAttendMeetings(intervals))

    def test_touching_intervals(self):
        intervals = [Interval(0, 8), Interval(8, 10)]
        self.assertTrue(self.s.canAttendMeetings(intervals))

    def test_conflict_simple(self):
        intervals = [Interval(0, 30), Interval(5, 10)]
        self.assertFalse(self.s.canAttendMeetings(intervals))

    def test_conflict_multiple(self):
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        self.assertFalse(self.s.canAttendMeetings(intervals))

    def test_out_of_order_input(self):
        intervals = [Interval(10, 20), Interval(0, 5), Interval(5, 10)]
        self.assertTrue(self.s.canAttendMeetings(intervals))

    def test_overlapping_chain(self):
        intervals = [Interval(1, 4), Interval(2, 5), Interval(5, 8)]
        self.assertFalse(self.s.canAttendMeetings(intervals))

    def test_large_values(self):
        intervals = [Interval(0, 1_000_000)]
        self.assertTrue(self.s.canAttendMeetings(intervals))


if __name__ == "__main__":
    unittest.main()
