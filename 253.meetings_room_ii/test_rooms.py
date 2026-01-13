import unittest
from rooms import Solution,Interval

class TestMinMeetingRooms(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.minMeetingRooms([]), 0)

    def test_single_meeting(self):
        intervals = [Interval(0, 10)]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 1)

    def test_no_overlap(self):
        intervals = [
            Interval(0, 5),
            Interval(5, 10),
            Interval(10, 15),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 1)

    def test_simple_overlap(self):
        intervals = [
            Interval(0, 30),
            Interval(5, 10),
            Interval(15, 20),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 2)

    def test_all_overlap(self):
        intervals = [
            Interval(1, 10),
            Interval(2, 9),
            Interval(3, 8),
            Interval(4, 7),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 4)

    def test_unsorted_input(self):
        intervals = [
            Interval(15, 20),
            Interval(0, 30),
            Interval(5, 10),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 2)

    def test_same_start_time(self):
        intervals = [
            Interval(0, 10),
            Interval(0, 5),
            Interval(0, 15),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 3)

    def test_same_end_time(self):
        intervals = [
            Interval(0, 10),
            Interval(5, 10),
            Interval(8, 10),
        ]
        self.assertEqual(self.sol.minMeetingRooms(intervals), 3)


if __name__ == "__main__":
    unittest.main()
