import unittest
from rooms import Solution


class TestMostBooked(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Room 0 holds meetings [0,10] and [2,7] (delayed), room 1 holds [1,5] and [3,4]
        self.assertEqual(self.solution.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]), 0)

    def test_example2(self):
        self.assertEqual(self.solution.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]), 1)

    def test_single_room(self):
        # Only one room, all meetings queued sequentially
        self.assertEqual(self.solution.mostBooked(1, [[0, 5], [5, 10], [10, 15]]), 0)

    def test_all_rooms_equal_count(self):
        # Each room gets exactly one meeting; lowest room number wins
        self.assertEqual(self.solution.mostBooked(2, [[0, 1], [1, 2]]), 0)

    def test_delayed_meeting_preserves_duration(self):
        # n=1, meetings [[0,5],[3,8]]: second meeting delayed to [5,10] (duration 5)
        # Room 0 holds both
        self.assertEqual(self.solution.mostBooked(1, [[0, 5], [3, 8]]), 0)

    def test_lowest_room_number_tiebreak(self):
        # Three rooms, each gets one meeting; room 0 should be returned
        self.assertEqual(self.solution.mostBooked(3, [[0, 1], [1, 2], [2, 3]]), 0)

    def test_many_meetings_one_room(self):
        meetings = [[i, i + 1] for i in range(10)]
        self.assertEqual(self.solution.mostBooked(1, meetings), 0)

    def test_large_gap_between_meetings(self):
        # Meetings far apart; room 0 handles all since it's always free
        self.assertEqual(self.solution.mostBooked(2, [[0, 1], [100, 101], [200, 201]]), 0)


if __name__ == "__main__":
    unittest.main()
